#!/usr/bin/env python3
"""Generate an engaging motion graphic MP4 video for Session 2.2 based on assets/session_2_2_campusjobs_pricing_hanji.png.
"""
import math
import subprocess
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
BASE_IMG_PATH = ROOT / "assets" / "session_2_2_campusjobs_pricing_hanji.png"
OUTPUT_MP4_PATH = ROOT / "assets" / "session_2_2_campusjobs_motion.mp4"

WIDTH = 1920
HEIGHT = 1080
FPS = 30
TOTAL_FRAMES = 840  # 28 seconds

# Fonts
FONT_SERIF_BOLD = "/home/sun/.local/share/fonts/timesbd.ttf"
FONT_SERIF_REG = "/home/sun/.local/share/fonts/times.ttf"
FONT_SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_SANS_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

f_title = ImageFont.truetype(FONT_SERIF_BOLD, 46)
f_sub = ImageFont.truetype(FONT_SANS_REG, 24)
f_sub_bold = ImageFont.truetype(FONT_SANS_BOLD, 25)
f_table_header = ImageFont.truetype(FONT_SERIF_BOLD, 30)
f_table_row = ImageFont.truetype(FONT_SERIF_REG, 26)
f_table_num = ImageFont.truetype(FONT_SERIF_BOLD, 28)
f_bubble = ImageFont.truetype(FONT_SANS_BOLD, 22)
f_stamp = ImageFont.truetype(FONT_SANS_BOLD, 36)
f_rule_title = ImageFont.truetype(FONT_SERIF_BOLD, 32)
f_rule_body = ImageFont.truetype(FONT_SANS_REG, 22)

def draw_bubble(draw, x, y, w, h, text, bg_color, border_color, text_color, tail_dir="down"):
    # Rounded speech bubble
    draw.rounded_rectangle([x, y, x + w, y + h], radius=14, fill=bg_color, outline=border_color, width=3)
    # Draw text centered
    lines = text.split("\n")
    total_text_h = len(lines) * 28
    start_y = y + (h - total_text_h) // 2
    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=f_bubble)
        tw = bbox[2] - bbox[0]
        draw.text((x + (w - tw) // 2, start_y + i * 28), line, fill=text_color, font=f_bubble)

def render_laptop_screen(draw, title_text, rows, header_bg=(19, 50, 80), text_color=(20, 30, 40)):
    # Laptop screen bounding box in 1920x1080: x: 745..1490, y: 460..975
    # Draw screen header
    draw.rectangle([748, 460, 1488, 540], fill=header_bg)
    bbox = draw.textbbox((0, 0), title_text, font=f_table_header)
    tw = bbox[2] - bbox[0]
    draw.text((748 + (740 - tw) // 2, 480), title_text, fill=(255, 255, 255), font=f_table_header)

    # Draw table body (cream background)
    draw.rectangle([748, 541, 1488, 970], fill=(245, 237, 225))

    y_cursor = 560
    for label, val, is_alert, is_success in rows:
        val_color = (220, 38, 38) if is_alert else ((16, 140, 75) if is_success else text_color)
        draw.text((790, y_cursor), label, fill=text_color, font=f_table_row)
        vbox = draw.textbbox((0, 0), val, font=f_table_num)
        vw = vbox[2] - vbox[0]
        draw.text((1440 - vw, y_cursor), val, fill=val_color, font=f_table_num)
        draw.line([790, y_cursor + 48, 1440, y_cursor + 48], fill=(210, 200, 185), width=1)
        y_cursor += 62

def render_frame(base_img, frame_idx):
    frame = base_img.copy()
    draw = ImageDraw.Draw(frame, "RGBA")

    # --- SUBTITLE BAR ---
    draw.rectangle([0, 1000, 1920, 1080], fill=(12, 18, 32, 240))
    # Top border for subtitle
    draw.line([0, 1000, 1920, 1000], fill=(56, 189, 248), width=3)

    # --- BEAT 1: Dilemma (0 - 150) ---
    if frame_idx < 150:
        pulse = (math.sin(frame_idx * 0.15) + 1) / 2
        # Highlight sticky note
        draw.rectangle([1505, 600, 1795, 870], outline=(245, 158, 11, int(150 + 105 * pulse)), width=4)
        
        # Subtitle
        draw.text((60, 1025), "SCENE 1 / THE TRAP: CampusJobs connects 6,000 students & 120 shops, but burns $4,000/mo.", fill=(255, 255, 255), font=f_sub_bold)
        draw.text((60, 1052), 'A friend advises Ravi: "Why not just charge everyone $2.00 a month? It sounds fair!"', fill=(148, 163, 184), font=f_sub)

    # --- BEAT 2: The Disaster of Equal Pricing (150 - 410) ---
    elif frame_idx < 410:
        rel = frame_idx - 150
        
        # Red highlight sticky note
        draw.rectangle([1505, 600, 1795, 870], fill=(254, 226, 226, 220), outline=(220, 38, 38), width=4)
        draw.text((1530, 680), "TESTING:\nCharge $2.00\nto Everyone!", fill=(185, 28, 28), font=f_table_header)

        # Student reaction (Left side)
        alpha_shake = int(math.sin(rel * 0.4) * 6)
        draw_bubble(draw, 80 + alpha_shake, 140, 340, 120, "😱 TOO EXPENSIVE!\n60% of students leave!\n(Only 2,400 remain)", (255, 241, 242), (244, 63, 94), (190, 18, 60))

        # Laptop Screen: Transitioning numbers
        progress = min(1.0, rel / 45.0)
        curr_students = int(6000 - 3600 * progress)
        curr_apps = int(9000 - 5400 * progress)
        apps_per_post = curr_apps / 300.0

        rows = [
            ("Students using app", f"{curr_students:,}", True, False),
            ("Shops posting jobs", "120", False, False),
            ("Job posts", "300", False, False),
            ("Applications", f"{curr_apps:,}", True, False),
            ("Apps per Job Post", f"{apps_per_post:.1f} (Threshold: 20)", True, False),
            ("Monthly Profit / Loss", "$5,040 - $4,000 = +$1,040?", True, False),
        ]
        render_laptop_screen(draw, "CampusJobs - Option A: Charge Everyone $2", rows, header_bg=(153, 27, 27))

        # Shop reaction (Right side)
        if rel > 40:
            draw_bubble(draw, 1460, 120, 380, 130, "😡 ONLY 12 APPLICANTS?!\nCan't find workers!\nI am abandoning this app!", (255, 241, 242), (244, 63, 94), (190, 18, 60))

        # Death Spiral Stamp
        if rel > 80:
            draw.rectangle([700, 340, 1540, 420], fill=(220, 38, 38, 235), outline=(255, 255, 255), width=3)
            draw.text((740, 355), "💥 DEATH SPIRAL: SYMMETRIC PRICING FAILS!", fill=(255, 255, 255), font=f_stamp)

        # Subtitle
        draw.text((60, 1025), "SCENE 2 / THE COLLAPSE: Students have high price sensitivity. 60% quit over $2.00!", fill=(254, 205, 211), font=f_sub_bold)
        draw.text((60, 1052), "Applications drop to 12 per post (below 20 min). Shops starve for workers and leave next!", fill=(255, 255, 255), font=f_sub)

    # --- BEAT 3: The Asymmetric Breakthrough (410 - 660) ---
    elif frame_idx < 660:
        rel = frame_idx - 410

        # Golden replacement sticky note
        draw.rectangle([1505, 600, 1795, 870], fill=(254, 243, 199, 235), outline=(217, 119, 6), width=4)
        draw.text((1530, 650), "THE SOLUTION:\n\nStudents: $0 FREE\nShops: $25 / Post", fill=(146, 64, 14), font=f_table_header)

        # Cheering Students (Left)
        draw_bubble(draw, 70, 130, 360, 130, "🎉 100% STUDENTS STAY!\nFree jobs app is awesome!\n(6,000 active candidates)", (240, 253, 244), (34, 197, 94), (21, 128, 61))

        # Laptop Screen: Green glowing table
        rows = [
            ("Students using app", "6,000 (FREE $0)", False, True),
            ("Shops posting jobs", "120 (Active)", False, True),
            ("Job posts", "300 posts", False, False),
            ("Applications", "9,000 applicants", False, True),
            ("Apps per Job Post", "30.0 (Target &ge; 20 Met! 🏆)", False, True),
            ("Revenue: 300 x $25", "$7,500 (Covers $4k Cost)", False, True),
        ]
        render_laptop_screen(draw, "CampusJobs - Option B: Asymmetric Pricing", rows, header_bg=(22, 101, 52))

        # Happy Shopkeeper (Right)
        draw_bubble(draw, 1450, 120, 400, 130, "☕ 30 APPLICANTS PER POST!\nHired a barista in 2 days!\n$25 is a total bargain!", (240, 253, 244), (34, 197, 94), (21, 128, 61))

        # Net Profit Laurel Stamp
        draw.rectangle([680, 335, 1560, 425], fill=(22, 101, 52, 235), outline=(250, 204, 21), width=3)
        draw.text((710, 355), "🏆 ASYMMETRIC WIN: +$3,500 NET PROFIT / MO!", fill=(255, 255, 255), font=f_stamp)

        # Subtitle
        draw.text((60, 1025), "SCENE 3 / THE ASYMMETRIC WIN: Keep students free ($0) to attract the crowd (Subsidy Side).", fill=(187, 247, 208), font=f_sub_bold)
        draw.text((60, 1052), "Charge shops $25 (Money Side). 300 x $25 = $7,500 revenue easily covers the $4,000 costs!", fill=(255, 255, 255), font=f_sub)

    # --- BEAT 4: The 4 Rules Summary (660 - 840) ---
    else:
        # Full screen elegant Hanji card overlay
        draw.rectangle([0, 0, 1920, 1080], fill=(248, 245, 239))
        draw.line([0, 0, 1920, 0], fill=(153, 27, 27), width=8)

        # Header
        draw.text((100, 50), "COURSE 1170 / DIGITAL TRANSFORMATION & PLATFORM STRATEGY", fill=(153, 27, 27), font=f_sub_bold)
        draw.text((100, 90), "Session 2.2: The 4 Golden Rules of Asymmetric Pricing", fill=(23, 32, 51), font=f_title)
        draw.line([100, 160, 1820, 160], fill=(201, 194, 182), width=2)

        rules = [
            ("RULE 1", "Subsidize the side that others come for",
             "Keep the magnet group free or cheap. Without 6,000 students, no shop will ever pay or post a job."),
            ("RULE 2", "Charge the side that gains the most from the match",
             "Shops save days of costly searching. That commercial value is worth far more than student cash."),
            ("RULE 3", "Check price sensitivity before setting a price",
             "Never assume. A $2 fee that looks tiny to a founder caused 60% of price-sensitive students to quit!"),
            ("RULE 4", "Make the money side cover the subsidy, and protect the free side",
             "Shop fees ($7,500) exceed platform costs ($4,000). Purge fake jobs to protect student trust."),
        ]

        card_y = 190
        for tag, title, desc in rules:
            draw.rectangle([100, card_y, 1820, card_y + 165], fill=(255, 255, 255), outline=(174, 183, 193), width=2)
            draw.rectangle([100, card_y, 108, card_y + 165], fill=(153, 27, 27))
            draw.text((130, card_y + 16), tag, fill=(153, 27, 27), font=f_sub_bold)
            draw.text((260, card_y + 14), title, fill=(23, 32, 51), font=f_rule_title)
            draw.text((130, card_y + 70), desc, fill=(53, 64, 82), font=f_rule_body)
            card_y += 185

        # Subtitle
        draw.text((60, 1025), "TAKEAWAY: Keep free the side others come for; charge the side that gains the most.", fill=(254, 240, 138), font=f_sub_bold)
        draw.text((60, 1052), "Session 2.2 Masterclass: Two-Sided Platform Pricing Architecture.", fill=(255, 255, 255), font=f_sub)

    return frame

def main():
    print(f"Loading base image: {BASE_IMG_PATH}")
    base_img = Image.open(BASE_IMG_PATH).resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)

    cmd = [
        "ffmpeg", "-y",
        "-f", "image2pipe",
        "-vcodec", "png",
        "-r", str(FPS),
        "-i", "-",
        "-vcodec", "libx264",
        "-pix_fmt", "yuv420p",
        "-crf", "18",
        str(OUTPUT_MP4_PATH)
    ]

    print(f"Rendering {TOTAL_FRAMES} frames ({TOTAL_FRAMES/FPS:.1f}s) to {OUTPUT_MP4_PATH}...")
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.PIPE)

    for i in range(TOTAL_FRAMES):
        frame = render_frame(base_img, i)
        frame.save(proc.stdin, "PNG")
        if i % 60 == 0:
            print(f"Rendered frame {i}/{TOTAL_FRAMES} ({(i/TOTAL_FRAMES)*100:.1f}%)")

    proc.stdin.close()
    proc.wait()
    print("Done! Exit code:", proc.returncode)
    print(f"Saved motion graphic video to: {OUTPUT_MP4_PATH}")

if __name__ == "__main__":
    main()
