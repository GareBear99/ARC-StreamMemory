from pathlib import Path
import sys, argparse, math
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path: sys.path.insert(0, str(ROOT_DIR))
from PIL import Image, ImageDraw
from scripts.common import write_json, utc_now

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--out', default='examples/demo_session')
    ap.add_argument('--frames', type=int, default=12)
    args = ap.parse_args()
    session = Path(args.out)
    frames = session / 'frames'
    frames.mkdir(parents=True, exist_ok=True)
    for i in range(args.frames):
        w, h = 1280, 720
        img = Image.new('RGB', (w, h), (7, 9, 18))
        d = ImageDraw.Draw(img)
        for x in range(0, w, 80): d.line((x, 0, x, h), fill=(24, 30, 55))
        for y in range(0, h, 80): d.line((0, y, w, y), fill=(24, 30, 55))
        cx = int(160 + (w - 320) * i / max(1, args.frames - 1))
        cy = int(h / 2 + math.sin(i * 0.6) * 120)
        d.ellipse((cx-56, cy-56, cx+56, cy+56), fill=(120, 70, 255), outline=(255, 110, 220), width=5)
        d.text((50, 50), 'ARC-StreamMemory Demo', fill=(245, 245, 255))
        d.text((50, 90), f'Frame {i+1}/{args.frames}', fill=(180, 200, 255))
        img.save(frames / f'frame_{i+1:06d}.png')
    write_json(session / 'memory' / 'capture_policy.json', {
        'capture_mode': 'demo_generated', 'ai_frame_rate': 1, 'raw_video_retained': False,
        'created_at': utc_now(), 'privacy': {'local_only': True, 'manual_capture': True, 'hidden_recording': False}
    })
    print(f'Created demo session: {session}')
if __name__ == '__main__': main()
