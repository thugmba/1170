#!/usr/bin/env python3
"""Render real 2D character puppet animation with lip-sync, blinking, gestures, and audio narration.
Outputs: assets/session_2_2_campusjobs_character_animation.mp4
"""
import math
import subprocess
import sys
import wave
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
BASE_IMG_PATH = ROOT / "assets" / "session_2_2_campusjobs_pricing_hanji.png"
AUDIO_PATH = Path("/tmp/final_audio.wav")
OUTPUT_MP4 = ROOT / "assets" / "session_2_2_campusjobs_character_animation.mp4"

WIDTH = 1920
HEIGHT = 1080
FPS = 30

# Load audio to calculate duration and RMS volume envelope for lip-sync
wf = wave.open(str(AUDIO_PATH), "rb")
n_frames = wf.getnframes()
rate = wf.getframerate()
raw_bytes = wf.readframes(n_frames)
wf.close()

samples = np.frombuffer(raw_bytes, dtype=np.int16).astype(np.float32) / 32768.0
total_sec = len(samples) / rate
total_video_frames = int(total_sec * FPS)

# Compute RMS per video frame
spf = int(rate / FPS)
rms_envelope = []
for i in range(total_video_frames):
    chunk = samples[i * spf : (i + 1) * spf]
    rms = np.sqrt(np.mean(chunk**2)) if len(chunk) > 0 else 0
    rms_envelope.append(float(rms))

print(f"Total video frames: {total_video_frames} ({total_sec:.2f}s at {FPS}fps)")

# Fonts
FONT_SERIF_BOLD = "/home/sun/.local/share/fonts/timesbd.ttf"
FONT_SERIF_REG = "/home/sun/.local/share/fonts/times.ttf"
FONT_SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_SANS_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

f_bubble_large = ImageFont.truetype(FONT_SERIF_BOLD, 40)
f_table_hdr = ImageFont.truetype(FONT_SERIF_BOLD, 30)
f_table_row = ImageFont.truetype(FONT_SERIF_REG, 26)
f_table_num = ImageFont.truetype(FONT_SERIF_BOLD, 28)
f_callout = ImageFont.truetype(FONT_SANS_BOLD, 22)
f_stamp = ImageFont.truetype(FONT_SANS_BOLD, 34)
f_sub_title = ImageFont.truetype(FONT_SANS_BOLD, 24)
f_sub_body = ImageFont.truetype(FONT_SANS_REG, 22)

# Load base image
base_img = Image.open(BASE_IMG_PATH).resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)

def draw_ravi_lip_sync(draw, t, rms, is_speaking):
    # Ravi's mouth location in 1920x1080 coordinates: (375, 550)
    mx, my = 373, 550
    # Skin tone background patch to cover default mouth
    draw.ellipse([mx - 18, my - 12, mx + 20, my + 14], fill=(245, 233, 218))

    if is_speaking and rms > 0.025:
        # Speaking mouth shapes
        w = int(14 + min(1.0, rms * 16) * 14)
        h = int(6 + min(1.0, rms * 20) * 14)
        # Mouth cavity
        draw.ellipse([mx - w//2, my - h//2, mx + w//2, my + h//2], fill=(95, 38, 32), outline=(55, 35, 30), width=1)
        # Upper teeth hint
        if h > 8:
            draw.rectangle([mx - w//3, my - h//2, mx + w//3, my - h//2 + 3], fill=(250, 248, 245))
        # Tongue hint
        if h > 10:
            draw.ellipse([mx - w//4, my + 1, mx + w//4, my + h//2], fill=(195, 85, 75))
    else:
        # Natural closed smiling/pondering mouth
        draw.arc([mx - 12, my - 4, mx + 12, my + 8], start=20, end=160, fill=(65, 45, 40), width=2)

def draw_ravi_eyes(draw, frame_idx):
    # Left eye: (344, 465), Right eye: (385, 473)
    # Blink every 95 frames (~3.2s) for 4 frames
    blink_cycle = frame_idx % 95
    if blink_cycle in (0, 1, 2, 3):
        # Draw eyelid closed arc
        for ex, ey in [(344, 465), (385, 473)]:
            draw.ellipse([ex - 9, ey - 9, ex + 9, ey + 9], fill=(245, 233, 218))
            draw.arc([ex - 8, ey - 4, ex + 8, ey + 6], start=190, end=350, fill=(55, 42, 38), width=3)

def draw_shopkeeper(draw, t, rms, frame_idx, scene):
    # Eyes: (1720, 365) & (1760, 362)
    # Mouth: (1725, 430)
    sx, sy = 1725, 430
    
    # Blinking (offset by 45 frames)
    blink = (frame_idx + 45) % 115
    if blink in (0, 1, 2):
        for ex, ey in [(1720, 365), (1760, 362)]:
            draw.ellipse([ex - 8, ey - 8, ex + 8, ey + 8], fill=(246, 234, 222))
            draw.arc([ex - 7, ey - 3, ex + 7, ey + 5], start=190, end=350, fill=(60, 45, 40), width=3)

    if scene == 2:
        # Upset / shouting in Scene 2
        draw.ellipse([sx - 16, sy - 14, sx + 18, sy + 18], fill=(246, 234, 222))
        draw.ellipse([sx - 12, sy - 10, sx + 14, sy + 14], fill=(95, 30, 25), outline=(55, 30, 25), width=2)
        # Steam puffs from hat
        puff_y = int(sy - 150 - (frame_idx % 30) * 2)
        draw.text((1710, puff_y), "♨️", fill=(220, 38, 38), font=f_callout)
    elif scene == 3:
        # Happy smiling eyes and smiling mouth
        draw.ellipse([sx - 16, sy - 12, sx + 18, sy + 14], fill=(246, 234, 222))
        draw.arc([sx - 14, sy - 8, sx + 14, sy + 10], start=10, end=170, fill=(55, 35, 30), width=3)
        # Cheerful eye crinkles
        for ex, ey in [(1720, 365), (1760, 362)]:
            draw.ellipse([ex - 8, ey - 8, ex + 8, ey + 8], fill=(246, 234, 222))
            draw.arc([ex - 7, ey - 4, ex + 7, ey + 4], start=200, end=340, fill=(55, 35, 30), width=3)

def draw_students(draw, frame_idx, scene):
    # Boy: (110, 470), Girl: (200, 476)
    # Blinking
    blink = (frame_idx + 20) % 105
    if blink in (0, 1, 2):
        for ex, ey in [(110, 470), (200, 476)]:
            draw.ellipse([ex - 7, ey - 7, ex + 7, ey + 7], fill=(245, 233, 218))
            draw.arc([ex - 6, ey - 3, ex + 6, ey + 4], start=190, end=350, fill=(55, 42, 38), width=2)

    if scene == 2:
        # Sad sweat drop
        draw.text((230, 420), "💧", fill=(56, 189, 248), font=f_callout)
    elif scene == 3:
        # Floating sparkles
        sparkle_y = int(380 - (frame_idx % 40) * 1.5)
        draw.text((210, sparkle_y), "✨", fill=(250, 204, 21), font=f_callout)

def render_screen(draw, title, rows, header_bg):
    # Laptop screen: x: 748..1488, y: 460..970
    draw.rectangle([748, 460, 1488, 540], fill=header_bg)
    bbox = draw.textbbox((0, 0), title, font=f_table_hdr)
    tw = bbox[2] - bbox[0]
    draw.text((748 + (740 - tw) // 2, 480), title, fill=(255, 255, 255), font=f_table_hdr)

    draw.rectangle([748, 541, 1488, 970], fill=(245, 237, 225))
    y_c = 560
    for label, val, is_alert, is_success in rows:
        v_col = (220, 38, 38) if is_alert else ((22, 101, 52) if is_success else (20, 30, 40))
        draw.text((790, y_c), label, fill=(20, 30, 40), font=f_table_row)
        vbox = draw.textbbox((0, 0), val, font=f_table_num)
        vw = vbox[2] - vbox[0]
        draw.text((1440 - vw, y_c), val, fill=v_col, font=f_table_num)
        draw.line([790, y_c + 48, 1440, y_c + 48], fill=(210, 200, 185), width=1)
        y_c += 62

def render_frame(frame_idx):
    t = frame_idx / float(FPS)
    rms = rms_envelope[min(frame_idx, len(rms_envelope) - 1)]
    frame = base_img.copy()
    draw = ImageDraw.Draw(frame, "RGBA")

    # Character Animation (Eye blinking, talking lip-sync)
    is_speaking = (rms > 0.02)
    draw_ravi_eyes(draw, frame_idx)
    draw_ravi_lip_sync(draw, t, rms, is_speaking)

    # Subtitle bar
    draw.rectangle([0, 1000, 1920, 1080], fill=(12, 18, 32, 245))
    draw.line([0, 1000, 1920, 1000], fill=(56, 189, 248), width=3)

    # --- SCENE DETERMINATION ---
    # 0.0 - 9.89s (0 - 296): Scene 1 Intro
    # 9.89 - 16.78s (296 - 503): Scene 1 Friend's Suggestion
    # 16.78 - 32.57s (503 - 977): Scene 2 Disaster / Collapse
    # 32.57 - 47.59s (977 - 1427): Scene 3 Asymmetric Win
    # 47.59 - 53.6s (1427 - end): Scene 4 The Golden Rule

    if t < 16.78:
        # Scene 1: Baseline & Dilemma
        scene = 1
        draw_shopkeeper(draw, t, rms, frame_idx, 1)
        draw_students(draw, frame_idx, 1)

        pulse = (math.sin(t * 4.0) + 1) / 2
        draw.rectangle([1505, 600, 1795, 870], outline=(245, 158, 11, int(140 + 115 * pulse)), width=4)

        if t < 9.89:
            draw.text((60, 1020), "SCENE 1: CampusJobs connects 6,000 students & 120 shops, but burns $4,000/mo.", fill=(255, 255, 255), font=f_sub_title)
            draw.text((60, 1050), "Ravi ponders: 'Who should pay: the students or the shops?'", fill=(148, 163, 184), font=f_sub_body)
        else:
            draw.text((60, 1020), "SCENE 1: A friend advises Ravi: 'Why not just charge everyone $2.00 a month?'", fill=(254, 240, 138), font=f_sub_title)
            draw.text((60, 1050), "Does equal pricing work on a two-sided platform?", fill=(255, 255, 255), font=f_sub_body)

    elif t < 32.57:
        # Scene 2: Disaster / Collapse
        scene = 2
        draw_shopkeeper(draw, t, rms, frame_idx, 2)
        draw_students(draw, frame_idx, 2)

        # Red sticky note
        draw.rectangle([1505, 600, 1795, 870], fill=(254, 226, 226, 220), outline=(220, 38, 38), width=4)
        draw.text((1530, 680), "TESTING:\nCharge $2.00\nto Everyone!", fill=(185, 28, 28), font=f_table_hdr)

        # Callouts
        draw.rectangle([60, 130, 420, 260], fill=(255, 241, 242), outline=(244, 63, 94), width=3)
        draw.text((80, 145), "😱 TOO EXPENSIVE!\n60% of students leave!\n(Only 2,400 remain)", fill=(190, 18, 60), font=f_callout)

        draw.rectangle([1450, 120, 1880, 260], fill=(255, 241, 242), outline=(244, 63, 94), width=3)
        draw.text((1470, 135), "😡 ONLY 12 APPLICANTS?!\nCan't find workers!\nI quit CampusJobs!", fill=(190, 18, 60), font=f_callout)

        # Laptop table
        rows = [
            ("Students using app", "2,400 (-60%)", True, False),
            ("Shops posting jobs", "120 (Leaving)", False, False),
            ("Job posts", "300 openings", False, False),
            ("Applications", "3,600 (-60%)", True, False),
            ("Apps per Job Post", "12.0 (Needs 20+!)", True, False),
            ("Monthly Revenue", "$5,040 (Fragile)", True, False),
        ]
        render_screen(draw, "Option A: Equal Fee ($2.00 / $2.00)", rows, (153, 27, 27))

        # Stamp
        draw.rectangle([680, 340, 1560, 425], fill=(220, 38, 38, 240), outline=(255, 255, 255), width=3)
        draw.text((710, 355), "💥 DEATH SPIRAL: EQUAL PRICING COLLAPSE!", fill=(255, 255, 255), font=f_stamp)

        draw.text((60, 1020), "SCENE 2 / COLLAPSE: Students have high price sensitivity. 60% quit over $2.00!", fill=(254, 205, 211), font=f_sub_title)
        draw.text((60, 1050), "Applications drop to 12 per post (below 20 min). Shops starve for workers and abandon the app!", fill=(255, 255, 255), font=f_sub_body)

    elif t < 47.59:
        # Scene 3: Asymmetric Win
        scene = 3
        draw_shopkeeper(draw, t, rms, frame_idx, 3)
        draw_students(draw, frame_idx, 3)

        # Lightbulb above Ravi
        draw.text((360, 310), "💡", fill=(250, 204, 21), font=f_callout)

        # Golden sticky note
        draw.rectangle([1505, 600, 1795, 870], fill=(254, 243, 199, 235), outline=(217, 119, 6), width=4)
        draw.text((1530, 650), "THE SOLUTION:\n\nStudents: $0 FREE\nShops: $25 / Post", fill=(146, 64, 14), font=f_table_hdr)

        # Cheerful Callouts
        draw.rectangle([60, 130, 430, 260], fill=(240, 253, 244), outline=(34, 197, 94), width=3)
        draw.text((80, 145), "🎉 100% STUDENTS STAY!\nFree jobs app is awesome!\n(6,000 active candidates)", fill=(21, 128, 61), font=f_callout)

        draw.rectangle([1440, 120, 1880, 260], fill=(240, 253, 244), outline=(34, 197, 94), width=3)
        draw.text((1460, 135), "☕ 30 APPLICANTS PER POST!\nHired a barista in 2 days!\n$25 is a total bargain!", fill=(21, 128, 61), font=f_callout)

        # Laptop table
        rows = [
            ("Students using app", "6,000 (100% FREE)", False, True),
            ("Shops posting jobs", "120 stores", False, True),
            ("Job posts", "300 openings", False, False),
            ("Applications", "9,000 applicants", False, True),
            ("Apps per Job Post", "30.0 (Target &ge; 20 Met! 🏆)", False, True),
            ("Revenue: 300 x $25", "$7,500 (+ $3,500 PROFIT)", False, True),
        ]
        render_screen(draw, "Option B: Asymmetric Pricing Strategy", rows, (22, 101, 52))

        # Stamp
        draw.rectangle([660, 335, 1580, 425], fill=(22, 101, 52, 240), outline=(250, 204, 21), width=3)
        draw.text((690, 355), "🏆 ASYMMETRIC WIN: +$3,500 NET PROFIT / MO!", fill=(255, 255, 255), font=f_stamp)

        draw.text((60, 1020), "SCENE 3 / BREAKTHROUGH: Subsidize the magnet side (Students = $0). Charge the money side ($25)!", fill=(187, 247, 208), font=f_sub_title)
        draw.text((60, 1050), "300 posts x $25 = $7,500 revenue easily covers the $4,000 costs, yielding $3,500 in sustainable profit!", fill=(255, 255, 255), font=f_sub_body)

    else:
        # Scene 4: The Golden Rule Card
        draw.rectangle([0, 0, 1920, 1080], fill=(248, 245, 239))
        draw.line([0, 0, 1920, 0], fill=(153, 27, 27), width=8)

        draw.text((100, 60), "COURSE 1170 / DIGITAL TRANSFORMATION & PLATFORM STRATEGY", fill=(153, 27, 27), font=f_sub_title)
        draw.text((100, 110), "Session 2.2: The Golden Rule of Asymmetric Pricing", fill=(23, 32, 51), font=f_bubble_large)
        draw.line([100, 180, 1820, 180], fill=(201, 194, 182), width=2)

        # Highlight box
        draw.rectangle([100, 230, 1820, 480], fill=(240, 253, 244), outline=(34, 197, 94), width=3)
        draw.text((150, 270), "THE GOLDEN TAKEAWAY:", fill=(21, 128, 61), font=f_sub_title)
        draw.text((150, 320), "Subsidize the side that others come for;\nCharge the side that gains the most from the match!", fill=(23, 32, 51), font=f_bubble_large)

        # Two pillars
        draw.rectangle([100, 520, 930, 880], fill=(255, 255, 255), outline=(174, 183, 193), width=2)
        draw.text((140, 550), "THE SUBSIDY SIDE (Students)", fill=(21, 128, 61), font=f_sub_title)
        draw.text((140, 600), "• Price: $0.00 FREE\n• High price sensitivity\n• Acts as the MAGNET that attracts the other side\n• Without them, the platform dies", fill=(53, 64, 82), font=f_callout)

        draw.rectangle([990, 520, 1820, 880], fill=(255, 255, 255), outline=(174, 183, 193), width=2)
        draw.text((1030, 550), "THE MONEY SIDE (Local Shops)", fill=(2, 132, 199), font=f_sub_title)
        draw.text((1030, 600), "• Price: $25.00 per job post\n• Low price sensitivity\n• Gains massive commercial value (saves hiring weeks)\n• Cross-subsidizes the free side", fill=(53, 64, 82), font=f_callout)

        draw.text((60, 1020), "CONCLUSION: Subsidize the side everyone comes for; charge the side that gains the most!", fill=(254, 240, 138), font=f_sub_title)
        draw.text((60, 1050), "Course 1170 · Digital Transformation & Platform Strategy", fill=(255, 255, 255), font=f_sub_body)

    return frame

def main():
    print(f"Rendering character animation video ({total_video_frames} frames, {total_sec:.1f}s)...")
    cmd = [
        "ffmpeg", "-y",
        "-f", "image2pipe",
        "-vcodec", "png",
        "-r", str(FPS),
        "-i", "-",
        "-i", str(AUDIO_PATH),
        "-vcodec", "libx264",
        "-pix_fmt", "yuv420p",
        "-acodec", "aac",
        "-b:a", "192k",
        "-crf", "18",
        "-shortest",
        str(OUTPUT_MP4)
    ]

    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    for i in range(total_video_frames):
        frame = render_frame(i)
        frame.save(proc.stdin, "PNG")
        if i % 150 == 0:
            print(f"Rendered frame {i}/{total_video_frames} ({(i/total_video_frames)*100:.1f}%)")

    proc.stdin.close()
    proc.wait()
    print("Done! Exit code:", proc.returncode)
    print(f"Character animated video saved to: {OUTPUT_MP4}")

if __name__ == "__main__":
    main()
