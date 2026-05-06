#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, datetime, shutil, subprocess
from pathlib import Path


def utc_now():
    return datetime.datetime.now(datetime.UTC).replace(microsecond=0).isoformat()


def main():
    ap=argparse.ArgumentParser(description='Build an ARC/FusionCapture-compatible capture_policy.json')
    ap.add_argument('--out', required=True, help='Session directory')
    ap.add_argument('--mode', default='inspection', choices=['navigation','inspection','blackbox','training','snapshot'])
    ap.add_argument('--ai-fps', type=float, default=1.0)
    ap.add_argument('--source', default=None)
    ap.add_argument('--raw-video-retained', action='store_true')
    args=ap.parse_args()
    session=Path(args.out)
    ffmpeg=shutil.which('ffmpeg')
    ffprobe=shutil.which('ffprobe')
    policy={
      'capture_mode':'arc_fusion_capture_adapter',
      'fusion_mode':args.mode,
      'ai_frame_rate':args.ai_fps,
      'source':args.source,
      'raw_video_retained':bool(args.raw_video_retained),
      'memory_tier': {'navigation':1,'inspection':2,'blackbox':2,'training':3,'snapshot':1}[args.mode],
      'created_at':utc_now(),
      'ffmpeg': {'ffmpeg_path':ffmpeg, 'ffprobe_path':ffprobe, 'backend':'regular_ffmpeg'},
      'privacy': {'local_only':True, 'manual_capture':True, 'hidden_recording':False}
    }
    p=session/'memory'/'capture_policy.json'; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(json.dumps(policy,indent=2)+'
')
    print(p)

if __name__=='__main__':
    main()
