# FFmpeg Backend

ARC-StreamMemory uses standard FFmpeg tooling for practical media ingest.

## Required tools

- `ffmpeg` for decoding video and extracting frames
- `ffprobe` for media metadata

Check availability:

```bash
python scripts/ffmpeg_probe.py
```

## Why FFmpeg remains the backend

FFmpeg is already the proven media engine. ARC-StreamMemory should not rewrite codecs. Instead, it controls:

- deterministic frame schedules
- AI-friendly frame rates
- capture policy JSON
- source hashes
- seed spine generation
- robotics/sensor metadata
- ARC receipts
- OmniBinary-style chunk maps
- Arc-RAR-style bundles

## Recommended frame rates

| AI FPS | Use case |
|---:|---|
| 0.2 | long passive memory |
| 0.5 | lightweight session archive |
| 1 | default AI visual memory |
| 2 | UI/debugging capture |
| 5 | interaction-heavy capture |
| 10 | high-motion review |

## Hardware acceleration notes

ARC-StreamMemory records available FFmpeg encoders/decoders when possible, but v2.1.0 does not require hardware acceleration. ARC-FusionCapture can later choose platform presets such as VideoToolbox, NVENC, Quick Sync, or VAAPI.
