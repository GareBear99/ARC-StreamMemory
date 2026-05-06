# Hardware Acceleration

FFmpeg can use platform-specific acceleration. ARC-StreamMemory v2.1.0 only detects and records capabilities.

Future ARC-FusionCapture profiles may select:

- macOS VideoToolbox
- NVIDIA NVENC
- Intel Quick Sync
- Linux VAAPI
- software fallback

The important rule is deterministic metadata: even when hardware acceleration is used, capture policy and FFmpeg command metadata must be stored in the session.
