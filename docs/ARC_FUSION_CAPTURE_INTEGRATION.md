# ARC-FusionCapture Integration

ARC-FusionCapture is the planned robotics/media orchestration layer around FFmpeg.

ARC-StreamMemory v2.1.0 is FusionCapture-compatible by exporting:

- capture policies
- frame schedules
- sensor sync records
- robotics session metadata
- ARC-style receipts
- OmniBinary-style chunk maps
- Arc-RAR-style manifests

## Division of responsibility

```text
ARC-FusionCapture
= camera/video/sensor capture orchestration, FFmpeg command selection, hardware profiles

ARC-StreamMemory
= memory session format, seed spine, module attachment, viewer, validation, bundle export
```

## Adapter command

```bash
python scripts/fusion_capture_adapter.py input.mp4 --mode inspection --ai-fps 2 --out sessions/inspection_memory
```

The adapter uses regular FFmpeg today and writes FusionCapture-style metadata for later robotics integration.
