from pathlib import Path
import sys
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path: sys.path.insert(0, str(ROOT_DIR))
import argparse, shutil, subprocess
from scripts.common import write_json, utc_now, sha256_file

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("video"); ap.add_argument("--fps", type=float, default=1.0); ap.add_argument("--out", required=True); args=ap.parse_args()
    if shutil.which("ffmpeg") is None: raise SystemExit("ffmpeg not found")
    video=Path(args.video); session=Path(args.out); frames=session/"frames"; frames.mkdir(parents=True, exist_ok=True)
    subprocess.run(["ffmpeg","-y","-i",str(video),"-vf",f"fps={args.fps}",str(frames/"frame_%06d.png")], check=True)
    write_json(session/"memory"/"capture_policy.json", {"capture_mode":"video_sample","source_video":str(video),"source_video_sha256":sha256_file(video),"ai_frame_rate":args.fps,"raw_video_retained":False,"created_at":utc_now(),"privacy":{"local_only":True,"manual_capture":True,"hidden_recording":False}})
    print(f"Sampled video: {session}")
if __name__=="__main__": main()
