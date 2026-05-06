#!/usr/bin/env python3
from __future__ import annotations
import argparse, subprocess, shutil, json, datetime, sys
from pathlib import Path


def utc_now():
    return datetime.datetime.now(datetime.UTC).replace(microsecond=0).isoformat()


def main():
    ap=argparse.ArgumentParser(description='ARC-FusionCapture-compatible adapter using regular FFmpeg.')
    ap.add_argument('input', help='Input video file')
    ap.add_argument('--mode', default='inspection', choices=['navigation','inspection','blackbox','training','snapshot'])
    ap.add_argument('--ai-fps', type=float, default=1.0)
    ap.add_argument('--out', required=True)
    ap.add_argument('--retain-video', action='store_true')
    args=ap.parse_args()

    ffmpeg=shutil.which('ffmpeg')
    ffprobe=shutil.which('ffprobe')
    if not ffmpeg:
        raise SystemExit('ffmpeg not found. Install ffmpeg or use snapshot ingest.')
    inp=Path(args.input)
    if not inp.exists():
        raise SystemExit(f'input not found: {inp}')
    session=Path(args.out)
    frames=session/'frames'; frames.mkdir(parents=True, exist_ok=True)
    cmd=[ffmpeg,'-y','-i',str(inp),'-vf',f'fps={args.ai_fps}',str(frames/'frame_%06d.png')]
    subprocess.run(cmd, check=True)

    if args.retain_video:
        video_dir=session/'video'; video_dir.mkdir(parents=True, exist_ok=True)
        # keep copy only if requested
        import shutil as _shutil
        _shutil.copy2(inp, video_dir/inp.name)

    policy={
      'capture_mode':'arc_fusion_capture_adapter',
      'fusion_mode':args.mode,
      'ai_frame_rate':args.ai_fps,
      'source_video':str(inp),
      'raw_video_retained':bool(args.retain_video),
      'memory_tier': {'navigation':1,'inspection':2,'blackbox':2,'training':3,'snapshot':1}[args.mode],
      'created_at':utc_now(),
      'ffmpeg': {'backend':'regular_ffmpeg','ffmpeg_path':ffmpeg,'ffprobe_path':ffprobe,'command':' '.join(cmd)},
      'privacy': {'local_only':True,'manual_capture':True,'hidden_recording':False}
    }
    p=session/'memory'/'capture_policy.json'; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(json.dumps(policy,indent=2)+'
')
    print(f'FusionCapture-compatible session frames written to {session}')
    print('Next: build_stream_memory.py, hash_memory_spine.py, build_seed_spine.py, build_ai_digest.py')

if __name__=='__main__':
    main()
