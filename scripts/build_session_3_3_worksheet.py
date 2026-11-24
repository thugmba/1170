"""Session 3.3 student answer sheet and answer key (Word).

Run: python3 scripts/build_session_3_3_worksheet.py
Out: worksheets/session_3_3_worksheet.docx, worksheets/session_3_3_worksheet_answer_key.docx
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import worksheet_lib as W  # noqa: E402
from worksheet_lib import (H1, H3, P, DO, TABLE, ANSWER_BOX, TASK,  # noqa: E402
                           given, head, inp, plain, para, runs)

SESSION = "3.3"
TITLE = "The Disruption Strategy"


def cover():
    key = W.ANSWERS
    out = [
        para(runs("Answer Sheet" + (" – ANSWER KEY" if key else ""), b=True, sz=32,
                  color=W.ANS if key else None), jc="center", before=0),
        para(runs(f"Session {SESSION}: {TITLE}", sz=26), jc="center", before=120, after=200),
        TABLE([[given("Name", b=True), inp("", 1), given("Student ID", b=True), inp("", 1), given("Date", b=True), inp("", 1, "YYYY-MM-DD")]],
              [0.8, 2.2, 1.1, 1.6, 0.7, 1.4], header=False, sz=20),
        TASK("\n1. Save this file as a **PDF**.\n2. Name it **StudentID_Name_S3.3.pdf** (example: 41234567_ChenWei_S3.3.pdf).\n"
             "3. Upload it to **iLearn** by the **end of class**.", label="HOW TO SUBMIT"),
        DO("Write in the yellow cells only. The blue text in each cell tells you what to write. "
           "The facts are on the lecture slides shown next to each heading."),
        DO("[Short] = a number, a word, or a calculation. [Written] = full sentences."),
    ]
    if key:
        out.append(P("**Teacher copy.** For open questions, the answer is an example; accept other answers with good reasons."))
    return out


CALC = "calculation = result"
SHORT = "**[Short]** "
WRITTEN = "**[Written]** "


def qa(rows, widths=(0.5, 4.0, 4.0)):
    """rows: (label, question, hint, answer, lines)."""
    return TABLE([[head("#"), head("Question"), head("Your answer")]]
                 + [[plain(a, b=True), q, inp(ans, n, h)] for a, q, h, ans, n in rows], list(widths))


def part1():
    return [
        H1("1. Warm-up (5 min) · Slides 2–6", newpage=False),
        DO("Answer each question in one sentence. Both are written answers."),
        qa([
            ("1", WRITTEN + "Who are Sweet Slice's non-consumers, and how many are there?",
             "who they are + how many people",
             "The 8,000 people who want a cake for a small celebration but buy none.", 2),
            ("2", WRITTEN + "Royal Cakes adds a $60 three-layer cake. Disruption or sustaining innovation? Why?",
             "disruption or sustaining + one reason",
             "Sustaining innovation: it is a better, more expensive product for Royal's best customers.", 2),
        ]),
    ]


def part2():
    return [
        H1("2. Tool Practice: SnapBox (during the lesson)", newpage=False),
        DO("For every calculation, write the calculation and the result, for example “60,000 x 30% = 18,000”."),
        H3("Tool 1 – Non-consumers · Slide 18"),
        qa([
            ("(a)", SHORT + "How many students need the job done?", CALC, "60,000 x 30% = 18,000 students", 2),
            ("(b)", SHORT + "How many are non-consumers?", CALC, "18,000 – 3,000 = 15,000 non-consumers", 2),
            ("(c)", SHORT + "How many studio customers are over-served?", CALC, "3,000 x 40% = 1,200 customers", 2),
            ("(d)", WRITTEN + "Which group should SnapBox start with, and which should it leave alone? (Rule 1)",
             "start with [group, number]; leave alone [group], because …",
             "Start with the 15,000 non-consumers (and the 1,200 over-served). Leave alone the other 1,800 studio "
             "customers who want a photographer: studios will fight for them (Rule 1).", 4),
        ]),
        H3("Tool 2 – The leader's profit test · Slide 20"),
        qa([
            ("(a)", SHORT + "Profit per customer: studio and SnapBox?", "Studio: calculation = result; SnapBox: calculation = result",
             "Studio: $80 – $40 = $40\nSnapBox: $6 – $3 = $3", 3),
            ("(b)", SHORT + "How many booth uses earn the profit of one studio session? (Round up.)", CALC + " (uses)",
             "$40 / $3 = 13.3, so 14 uses", 2),
            ("(c)", SHORT + "One day: a lobby booth (40 uses) vs one photographer (8 sessions)?",
             "Booth: calculation = $ a day; Photographer: calculation = $ a day",
             "Booth: 40 x $3 = $120 a day\nPhotographer: 8 x $40 = $320 a day", 3),
            ("(d)", WRITTEN + "Will studios copy SnapBox? What will they do instead?",
             "Yes / No, because …; instead they will …",
             "Probably not: copying earns much less. Studios will more likely improve sessions for their best "
             "customers, e.g. a $120 premium session (sustaining innovation, Rule 3).", 4),
        ]),
        H3("Tool 3 – Profit over several periods · Slide 22"),
        qa([
            ("(a)", SHORT + "30 uses a day: profit a month after rent, and over 12 months?",
             "a month: calculation = result; 12 months: calculation = result",
             "900 x $3 = $2,700; $2,700 – $700 = $2,000 a month\n12 x $2,000 – $4,000 = $20,000", 3),
            ("(b)", SHORT + "Months to earn back the $4,000?", CALC + " (months)", "$4,000 / $2,000 = 2 months", 2),
            ("(c)", SHORT + "15 uses a day: profit over 12 months?", "a month, then 12 months: calculation = result",
             "450 x $3 = $1,350; – $700 = $650 a month\n12 x $650 – $4,000 = $3,800", 3),
            ("(d)", SHORT + "Smallest number of uses a day for a 12-month profit of $0 or more? (Round up.)",
             CALC + " (uses a day)",
             "$333 + $700 = $1,033 a month; / $3 = 344 uses; / 30 = 11.5, so 12 uses a day", 3),
        ]),
        H3("Tool 4 – Trade-off and decision rule · Slide 24"),
        qa([
            ("(a)", SHORT + "5 booths: 12-month profit at 30, 15, and 8 uses a day?",
             "one line for each: 30 uses / 15 uses / 8 uses",
             "30 uses: 5 x $20,000 = $100,000\n15 uses: 5 x $3,800 = $19,000\n"
             "8 uses: 240 x $3 – $700 = $20 a month; 12 x $20 – $4,000 = –$3,760; x 5 = –$18,800", 4),
            ("(b)", WRITTEN + "Trade-off: what does 1 booth first give up, and what does it protect?",
             "It gives up $… to protect against …",
             "It gives up up to $80,000 extra profit in the best case ($100,000 – $20,000) to protect itself "
             "from an $18,800 loss if demand is low (one weak booth loses only $3,760).", 3),
            ("(c)", SHORT + "Which rule supports starting with one booth?", "Rule number + its name",
             "Rule 4: improve step by step before growing fast.", 2),
            ("(d)", WRITTEN + "Decision rule (a number, a time, and an action):",
             "If [number] by [time], we will [action].",
             "“If the first booth averages at least 12 uses a day for two months, we will open four more; "
             "if not, we will move it to a busier street.”", 3),
        ]),
        H3("Put it together"),
        DO("Written answer: Is SnapBox a real disruption? How fast should it grow? Answer in 2–3 sentences."),
        ANSWER_BOX("Yes. It starts with 15,000 non-consumers (Rule 1), offers simple $6 photos that are good enough "
                   "(Rule 2), and studios earn much more per customer, so they will not copy it (Rule 3). "
                   "It should start with one booth and open more only after the first booth reaches about 12 uses a day (Rule 4).",
                   4, hint="Yes / No + Rules 1–3 with numbers + how fast to grow (Rule 4)"),
    ]


def part3():
    ex = [
        ("(a) $3 rice-box stand",
         "Non-consumers (students who skip lunch)", "Simpler and cheaper", "Disruption", "Rules 1 and 2"),
        ("(b) Steak house $120 chef's table",
         "The leader's best customers", "Better and more expensive", "Not disruption (sustaining)", "Rule 1"),
        ("(c) Free photo-light app",
         "Non-consumers who would never pay a studio", "Simpler and cheaper", "Disruption", "Rules 1 and 2"),
        ("(d) Coffee chain gold card",
         "The leader's best customers", "Better (for them)", "Not disruption (sustaining)", "Rule 1"),
        ("(e) $10 online cooking videos",
         "Non-consumers and over-served", "Simpler and cheaper", "Disruption", "Rules 1 and 2"),
        ("(f) Fourth camera on top phone",
         "The leader's best customers", "Better and more expensive", "Not disruption (sustaining)", "Rule 1"),
    ]
    rows = [[head("Case"), head("First customers"), head("Simpler & cheaper, or better & pricier?"),
             head("Disruption or not?"), head("Rule")],
            [given("Choose one:"), given("non-consumers / over-served / the leader's best"),
             given("simpler & cheaper / better & pricier"), given("disruption / not disruption"), given("rule no.")]]
    rows += [[plain(p)] + [inp(a, 2) for a in ans] for p, *ans in ex]
    return [
        H1("3. Exercise 1 – Disruption or Not? (20 min) · Slide 25", newpage=False),
        DO("Short answers: for each case, fill in the four yellow cells. Choose from the options in the grey row."),
        TABLE(rows, [2.0, 2.2, 1.8, 1.5, 0.9], sz=19),
    ]


def part4():
    calc = [
        ("1", SHORT + "Non-consumers", "men", "50,000 – 20,000 = 30,000 men"),
        ("2", SHORT + "Salon profit per haircut", "$", "$40 – $25 = $15"),
        ("3", SHORT + "QuickCut profit per haircut", "$", "$8 – $5 = $3"),
        ("4", SHORT + "How many times more a salon earns per haircut", "times", "$15 / $3 = 5 times"),
        ("5", SHORT + "QuickCut haircuts a month", "haircuts", "30,000 x 10% = 3,000 haircuts"),
        ("6", SHORT + "QuickCut profit a month", "$", "3,000 x $3 = $9,000"),
        ("7", SHORT + "Profit over 12 months", "$", "12 x $9,000 – 3 x $6,000 = $108,000 – $18,000 = $90,000"),
    ]
    rules = [
        ("Rule 1", "Our first customers are [who], [number] people.",
         "Our first customers are the men who cut their hair at home, 30,000 people (plus salon customers who only want a quick cut)."),
        ("Rule 2", "We do [the main job] for $[price] instead of $[leader's price]; we leave out [what].",
         "We give a clean haircut for $8 instead of $40; we leave out washing, styling, and booking."),
        ("Rule 3", "The leader earns $[number] per customer; copying us earns $[number].",
         "Salons earn $15 a haircut; copying us earns $3, five times less."),
        ("Rule 4", "First we [first step]; later we [how we move up].",
         "First we open one shop in a busy station; later we add more stations and simple extras such as beard trims."),
        ("Verdict", "[Go / Do not go], because [one sentence].",
         "Go, because 30,000 men are not served and salons will not fight for a $3-profit haircut."),
    ]
    return [
        H1("4. Exercise 2 – QuickCut (30 min) · Slides 26–28", newpage=False),
        H3("Step 1 – Calculation · Slide 27"),
        DO("Fill in the rows in order. Later rows use earlier rows."),
        TABLE([[head("#"), head("What to calculate"), head("Your calculation and answer")]]
              + [[plain(a, b=True), q, inp(ans, 2, f"{CALC} ({u})")] for a, q, u, ans in calc],
              [0.4, 3.6, 4.6]),
        H3("Step 2 – Rule check and verdict · Slide 28"),
        DO("Written answers: copy the sentence in blue and replace every [bracket] with your numbers from Step 1."),
        TABLE([[head("Rule"), head("Your sentence")]]
              + [[plain(r, b=True), inp(a, 3, f)] for r, f, a in rules],
              [1.2, 7.4]),
    ]


def part5():
    calc = [
        ("1", SHORT + "Option A: profit a month (600 cakes)", "600 x $10 = $6,000"),
        ("2", SHORT + "Option A: profit over 12 months", "12 x $6,000 – $20,000 = $52,000"),
        ("3", SHORT + "Option A: profit a month if Royal cuts its price (200 cakes)", "200 x $10 = $2,000"),
        ("4", SHORT + "Option A: profit over 12 months if Royal cuts its price", "12 x $2,000 – $20,000 = $4,000"),
        ("5", SHORT + "Option B: regular customers", "8,000 x 10% = 800 customers"),
        ("6", SHORT + "Option B: slices a month", "800 x 3 = 2,400 slices"),
        ("7", SHORT + "Option B: profit a month", "2,400 x $2 = $4,800"),
        ("8", SHORT + "Option B: profit over 12 months", "12 x $4,800 – $5,000 = $52,600"),
    ]
    memo = [
        ("To:", "[name], [role]", "Mr. Carter, investor, Sweet Slice", 1),
        ("1. Decision and evidence", "We should choose [option] because [rule] and [one number from Step 1].",
         "We should choose Option B, because it serves the 8,000 people nobody serves (Rule 1) and Royal will not copy a $2-slice model (Rule 3). "
         "It earns $52,600, about the same as Option A's best case, without depending on Royal.", 3),
        ("2. Biggest risk and trade-off", "The weakest point is [risk]. We give up [what we lose] to gain [what we win].",
         "The weakest point is that fewer than 10% of non-consumers may come. We give up the higher price of whole cakes "
         "to avoid a price war that could cut Option A to $4,000.", 3),
        ("3. Next step and decision rule", "In the next 3 months we will [action] and measure [number]. "
         "We will change this decision if [result].",
         "In the next three months we will advertise on campus and count slices sold each week. "
         "We will change the price or the menu if we sell fewer than 450 slices a week by the end of month 3.", 3),
    ]
    return [
        H1("5. Exercise 3 – Sweet Slice: Option A or B? (50 min) · Slides 29–31", newpage=False),
        H3("Step 1 – Calculation · Slide 30"),
        DO("Fill in the rows in order. Rows 1–4 are Option A; rows 5–8 are Option B."),
        TABLE([[head("#"), head("What to calculate"), head("Your calculation and answer")]]
              + [[plain(a, b=True), q, inp(ans, 2, CALC)] for a, q, ans in calc]
              + [[plain("9", b=True), WRITTEN + "Would Royal copy Option A? Option B?",
                  inp("B: less ($2 a slice vs $15 a cake), so Royal ignores it.\n"
                      "A: same kind of cake, so Royal can easily copy or cut its price.", 2,
                      "A: Yes / No, because …; B: Yes / No, because …")]],
              [0.4, 3.6, 4.6]),
        H3("Step 2 – Memo to the investor · Slide 31"),
        DO("Written answers: choose Option A or B. Copy the sentence in blue and replace every [bracket]. "
           "Then present your memo in 2 minutes."),
        TABLE([[head("Bullet"), head("Your memo")]]
              + [[plain(r, b=True), inp(a, n, f)] for r, f, a, n in memo],
              [2.0, 6.6]),
    ]


def blocks():
    return cover() + part1() + part2() + part3() + part4() + part5()


if __name__ == "__main__":
    out = os.path.join(W.ROOT, "worksheets")
    W.build(blocks, os.path.join(out, "session_3_3_worksheet.docx"))
    W.build(blocks, os.path.join(out, "session_3_3_worksheet_answer_key.docx"), answers=True)
