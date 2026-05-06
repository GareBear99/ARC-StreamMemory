# ARC-FusionCapture Integration

This directory defines how ARC-StreamMemory interoperates with the planned ARC-FusionCapture runtime.

v2.1.0 uses regular FFmpeg today through:

- `scripts/ffmpeg_probe.py`
- `scripts/fusion_capture_adapter.py`
- `scripts/build_capture_policy.py`
- `scripts/sync_sensor_log.py`

A future standalone ARC-FusionCapture repo can call ARC-StreamMemory scripts or write the same session layout directly.
