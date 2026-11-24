"""Build student worksheets (.docx) on top of templates/Final_Project_Report_Template.docx.

The template gives the page setup, fonts, heading styles, header, and page-number footer.
This module only replaces the body. Colour code used in every worksheet:
  yellow cell  = the student writes here
  blue italic  = instructions (what to do)
  grey cell    = given facts or a finished example
Call build(blocks, out_path, answers=False). With answers=True, every yellow cell shows
the answer in dark red (teacher copy).
"""
import os
import re
import shutil
import tempfile
import zipfile
from xml.sax.saxutils import escape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "templates", "Final_Project_Report_Template.docx")

YELLOW = "FFF2CC"
GREY = "F2F2F2"
HEAD = "E7E6E6"
BLUE = "1F4E79"
GREY_TXT = "404040"
ANS = "C00000"
PAGE_W = 9026  # text width in dxa (A4 minus 2.54 cm margins)

ANSWERS = False


# ---------- runs and paragraphs ----------
def _run(text, b=False, i=False, color=None, sz=None):
    rpr = ""
    if b:
        rpr += "<w:b/><w:bCs/>"
    if i:
        rpr += "<w:i/><w:iCs/>"
    if color:
        rpr += f'<w:color w:val="{color}"/>'
    if sz:
        rpr += f'<w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/>'
    rpr = f"<w:rPr>{rpr}</w:rPr>" if rpr else ""
    parts = str(text).split("\n")
    out = ""
    for k, part in enumerate(parts):
        if k:
            out += f"<w:r>{rpr}<w:br/></w:r>"
        out += f'<w:r>{rpr}<w:t xml:space="preserve">{escape(part)}</w:t></w:r>'
    return out


def runs(text, **base):
    """Text with **bold** marks -> runs."""
    out = ""
    for k, part in enumerate(re.split(r"\*\*", str(text))):
        if part:
            out += _run(part, b=base.get("b", False) or k % 2 == 1, i=base.get("i", False),
                        color=base.get("color"), sz=base.get("sz"))
    return out


def para(content, style=None, jc=None, before=None, after=None, line=None, keep=False, num=None, ind=None, newpage=False):
    ppr = ""
    if style:
        ppr += f'<w:pStyle w:val="{style}"/>'
    if newpage:
        ppr += "<w:pageBreakBefore/>"
    if keep:
        ppr += "<w:keepNext/>"
    if num:
        ppr += f'<w:numPr><w:ilvl w:val="0"/><w:numId w:val="{num}"/></w:numPr>'
    sp = ""
    if before is not None:
        sp += f' w:before="{before}"'
    if after is not None:
        sp += f' w:after="{after}"'
    if line is not None:
        sp += f' w:line="{line}" w:lineRule="auto"'
    if sp:
        ppr += f"<w:spacing{sp}/>"
    if ind:
        ppr += f'<w:ind w:left="{ind}"/>'
    if jc:
        ppr += f'<w:jc w:val="{jc}"/>'
    return f"<w:p><w:pPr>{ppr}</w:pPr>{content}</w:p>"


def H1(t, newpage=True):
    return para(runs(t), "Heading1", newpage=newpage)


def H2(t):
    return para(runs(t), "Heading2")


def H3(t):
    return para(runs(t), "Heading3")


def P(t, **kw):
    return para(runs(t), **kw)


def DO(t):
    """Blue instruction line."""
    return para(_run("➜ ", b=True, color=BLUE) + runs(t, i=True, color=BLUE), keep=True)


def BUL(t, color=None, i=False):
    return para(runs(t, color=color, i=i), "ListParagraph", num=2, after=40)


def PAGEBREAK():
    return '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'


def CAPTION(t):
    return para(runs(t, b=True, sz=20), before=120, after=60, keep=True)


# ---------- tables ----------
def _border(color="808080", sz=4):
    return "".join(f'<w:{s} w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
                   for s in ("top", "left", "bottom", "right"))


def given(t, b=False):
    return {"kind": "given", "text": t, "b": b}


def head(t):
    return {"kind": "head", "text": t}


def inp(answer="", lines=1, hint=""):
    """Yellow cell. hint = short blue text shown in the student copy."""
    return {"kind": "input", "answer": answer, "lines": lines, "hint": hint}


def plain(t, b=False):
    return {"kind": "plain", "text": t, "b": b}


def _cell(c, w, sz=20):
    if isinstance(c, str):
        c = plain(c)
    kind = c["kind"]
    fill = {"head": HEAD, "given": GREY, "input": YELLOW}.get(kind)
    shd = f'<w:shd w:val="clear" w:color="auto" w:fill="{fill}"/>' if fill else ""
    tcpr = (f'<w:tcPr><w:tcW w:w="{w}" w:type="dxa"/><w:tcBorders>{_border("404040", 8) if kind == "input" else _border()}</w:tcBorders>{shd}'
            '<w:tcMar><w:top w:w="60" w:type="dxa"/><w:left w:w="100" w:type="dxa"/>'
            '<w:bottom w:w="60" w:type="dxa"/><w:right w:w="100" w:type="dxa"/></w:tcMar></w:tcPr>')
    sp = dict(after=0, line=240)
    if kind == "head":
        body = "".join(para(runs(x, b=True, sz=sz), **sp) for x in c["text"].split("\n"))
    elif kind == "input":
        if ANSWERS and c["answer"]:
            body = "".join(para(runs(x, b=True, color=ANS, sz=sz), **sp) for x in c["answer"].split("\n"))
        else:
            body = para(runs(c["hint"], i=True, color=BLUE, sz=18), **sp) if c["hint"] else para("", **sp)
            body += "".join(para("", **sp) for _ in range(max(c["lines"] - (1 if c["hint"] else 0), 0)))
            if not c["hint"] and c["lines"] <= 1:
                body = para("", **sp)
    else:
        color = GREY_TXT if kind == "given" else None
        body = "".join(para(runs(x, b=c.get("b", False), color=color, sz=sz), **sp)
                       for x in c["text"].split("\n"))
    return f"<w:tc>{tcpr}{body}</w:tc>"


def TABLE(rows, widths, header=True, sz=20, caption=None):
    """rows: list of lists of cells (str -> plain). widths: relative numbers."""
    tot = sum(widths)
    ws = [round(PAGE_W * x / tot) for x in widths]
    ws[-1] = PAGE_W - sum(ws[:-1])
    grid = "".join(f'<w:gridCol w:w="{w}"/>' for w in ws)
    out = (f'<w:tbl><w:tblPr><w:tblW w:w="{PAGE_W}" w:type="dxa"/><w:tblBorders>{_border("auto")}'
           '<w:insideH w:val="single" w:sz="4" w:space="0" w:color="auto"/>'
           '<w:insideV w:val="single" w:sz="4" w:space="0" w:color="auto"/></w:tblBorders>'
           '<w:tblLayout w:type="fixed"/>'
           f'<w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0" w:firstColumn="1" w:lastColumn="0" w:noHBand="0" w:noVBand="1"/>'
           f"</w:tblPr><w:tblGrid>{grid}</w:tblGrid>")
    for k, r in enumerate(rows):
        trpr = "<w:trPr><w:cantSplit/>" + ("<w:tblHeader/>" if header and k == 0 else "") + "</w:trPr>"
        out += f"<w:tr>{trpr}" + "".join(_cell(c, ws[j], sz) for j, c in enumerate(r)) + "</w:tr>"
    out += "</w:tbl>"
    pre = CAPTION(caption) if caption else ""
    return pre + out + para("", after=60)


def BOX(lines, kind="given", title=None):
    """One-cell box. lines: list of strings (grey box) or an inp() cell."""
    if isinstance(lines, dict):
        cell = lines
    else:
        txt = ((f"**{title}**\n") if title else "") + "\n".join(lines)
        cell = {"kind": kind, "text": txt, "b": False}
    return TABLE([[cell]], [1], header=False, sz=22)


def ANSWER_BOX(answer, lines=3, hint="Write your answer here."):
    return TABLE([[inp(answer, lines, hint)]], [1], header=False, sz=22)


def TASK(text, label="Your task: "):
    """Blue-bordered 'Your task' box."""
    tcpr = (f'<w:tcPr><w:tcW w:w="{PAGE_W}" w:type="dxa"/><w:tcBorders>'
            + "".join(f'<w:{s} w:val="single" w:sz="12" w:space="0" w:color="{BLUE}"/>' for s in ("top", "left", "bottom", "right"))
            + '</w:tcBorders><w:shd w:val="clear" w:color="auto" w:fill="DEEAF6"/>'
            '<w:tcMar><w:top w:w="100" w:type="dxa"/><w:left w:w="140" w:type="dxa"/><w:bottom w:w="100" w:type="dxa"/>'
            '<w:right w:w="140" w:type="dxa"/></w:tcMar></w:tcPr>')
    body = "".join(para((_run(label, b=True, color=BLUE) if k == 0 else "") + runs(t, color=BLUE), after=0, line=276)
                   for k, t in enumerate(text.split("\n")))
    return (f'<w:tbl><w:tblPr><w:tblW w:w="{PAGE_W}" w:type="dxa"/><w:tblLayout w:type="fixed"/></w:tblPr>'
            f'<w:tblGrid><w:gridCol w:w="{PAGE_W}"/></w:tblGrid><w:tr><w:tc>{tcpr}{body}</w:tc></w:tr></w:tbl>'
            + para("", after=60))


def CHECK(t):
    return para(_run("☐  ", sz=26) + runs(t), after=60, ind=360)


# ---------- assemble ----------
def build(blocks_fn, out_path, answers=False):
    global ANSWERS
    ANSWERS = answers
    body = "".join(blocks_fn())
    tmp = tempfile.mkdtemp()
    with zipfile.ZipFile(TEMPLATE) as z:
        z.extractall(tmp)
    docp = os.path.join(tmp, "word", "document.xml")
    d = open(docp, encoding="utf-8").read()
    start = d.index("<w:body>") + len("<w:body>")
    sect = re.findall(r"<w:sectPr\b.*?</w:sectPr>", d, re.S)[-1]
    d = d[:start] + body + sect + "</w:body></w:document>"
    open(docp, "w", encoding="utf-8").write(d)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    if os.path.exists(out_path):
        os.remove(out_path)
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as z:
        for dp, _, fs in os.walk(tmp):
            for f in fs:
                full = os.path.join(dp, f)
                z.write(full, os.path.relpath(full, tmp))
    shutil.rmtree(tmp)
    print("wrote", out_path)
