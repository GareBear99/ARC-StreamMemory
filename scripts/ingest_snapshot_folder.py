from pathlib import Path
import sys
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path: sys.path.insert(0, str(ROOT_DIR))
from PIL import Image
import argparse
from scripts.common import write_json, utc_now
EXTS={".png",".jpg",".jpeg",".webp",".bmp"}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("folder"); ap.add_argument("--out", required=True); args=ap.parse_args()
    src=Path(args.folder); session=Path(args.out); frames=session/"frames"; frames.mkdir(parents=True, exist_ok=True)
    imgs=sorted([p for p in src.iterdir() if p.suffix.lower() in EXTS])
    if not imgs: raise SystemExit("No images found")
    for i,p in enumerate(imgs,1): Image.open(p).convert("RGB").save(frames/f"frame_{i:06d}.png")
    write_json(session/"memory"/"capture_policy.json", {"capture_mode":"snapshot_folder","source_folder":str(src),"ai_frame_rate":1,"raw_video_retained":False,"created_at":utc_now(),"privacy":{"local_only":True,"manual_capture":True,"hidden_recording":False}})
    print(f"Ingested {len(imgs)} snapshots")
if __name__=="__main__": main()
