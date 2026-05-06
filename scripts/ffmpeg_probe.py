#!/usr/bin/env python3
from __future__ import annotations
import shutil, subprocess, json, argparse
from pathlib import Path


def run(cmd):
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        return {'ok': out.returncode == 0, 'stdout': out.stdout[:4000], 'stderr': out.stderr[:4000]}
    except Exception as e:
        return {'ok': False, 'error': str(e)}


def main():
    ap = argparse.ArgumentParser(description='Probe FFmpeg / FFprobe availability and capabilities.')
    ap.add_argument('--json-out', default=None, help='Optional JSON report output path.')
    args = ap.parse_args()

    ffmpeg = shutil.which('ffmpeg')
    ffprobe = shutil.which('ffprobe')
    report = {
        'ffmpeg_path': ffmpeg,
        'ffprobe_path': ffprobe,
        'ffmpeg_version': run([ffmpeg, '-version']) if ffmpeg else {'ok': False, 'error': 'ffmpeg not found'},
        'ffprobe_version': run([ffprobe, '-version']) if ffprobe else {'ok': False, 'error': 'ffprobe not found'},
        'encoders': run([ffmpeg, '-hide_banner', '-encoders']) if ffmpeg else {'ok': False},
        'decoders': run([ffmpeg, '-hide_banner', '-decoders']) if ffmpeg else {'ok': False}
    }
    print(json.dumps(report, indent=2))
    if args.json_out:
        p=Path(args.json_out); p.parent.mkdir(parents=True, exist_ok=True); p.write_text(json.dumps(report, indent=2)+'
')

if __name__ == '__main__':
    main()
