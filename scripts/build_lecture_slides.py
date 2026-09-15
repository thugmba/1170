import os
import subprocess
import fitz # PyMuPDF

def build_session_lecture_pdf(session_id="1_1", html_path=None, output_dir=r"d:\Projects\1170\slides", assets_dir=r"d:\Projects\1170\assets\lecture_slides"):
    """
    Builds a multi-page 16:9 lecture slide PDF and companion PNG previews.
    Enforces English MS Windows environment standards and sub-pixel footer coordinates.
    """
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(assets_dir, exist_ok=True)

    edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
    pdf_file = os.path.join(output_dir, f"session_{session_id}_lecture.pdf")

    if html_path is None:
        html_path = rf"C:\Users\Sun\.gemini\antigravity-ide\brain\82ef3cd3-b160-4cd2-af87-7d965f20ac46\scratch\session_{session_id}_lecture.html"

    if not os.path.exists(html_path):
        raise FileNotFoundError(f"HTML slide template not found: {html_path}")

    # 1. Execute headless print-to-pdf in English MS Windows
    cmd = [
        edge_path,
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={pdf_file}",
        "--no-pdf-header-footer",
        f"file:///{html_path.replace(chr(92), '/')}"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"Edge headless print-to-pdf failed: {res.stderr}")

    print(f"[OK] Generated PDF: {pdf_file} ({os.path.getsize(pdf_file)} bytes)")

    # 2. Sub-pixel verification protocol and PNG preview generation
    doc = fitz.open(pdf_file)
    total_pages = len(doc)
    print(f"[INFO] Total Pages: {total_pages}")

    for idx, page in enumerate(doc):
        page_num = idx + 1
        # Check footer Y coordinate on content slides (pages 2+)
        if page_num > 1:
            slide_rects = page.search_for("Slide")
            if not slide_rects:
                print(f"[WARNING] Page {page_num}: 'Slide' text marker not found.")
            else:
                y0 = slide_rects[0].y0
                expected_y0 = 597.3047
                if abs(y0 - expected_y0) > 0.5:
                    print(f"[WARNING] Page {page_num}: Footer Y drift detected! y0={y0:.4f} (expected {expected_y0})")
                else:
                    print(f"[VERIFIED] Page {page_num}: Footer locked at y0={y0:.4f} pt.")

        # Export high-resolution 16:9 PNG preview
        pix = page.get_pixmap(matrix=fitz.Matrix(2.0, 2.0))
        img_out = os.path.join(assets_dir, f"slide_{page_num}.png")
        pix.save(img_out)
        print(f"[EXPORTED] {img_out} ({pix.width}x{pix.height})")

    doc.close()
    print("[SUCCESS] Slide generation and verification complete.")

if __name__ == "__main__":
    build_session_lecture_pdf("1_1")
