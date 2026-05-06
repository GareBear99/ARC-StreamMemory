# FFmpeg + ARC-FusionCapture Audit

v2.1.0 adds a regular FFmpeg path and a FusionCapture-compatible adapter without making false claims about native robotics capture being complete.

Complete now:

- ffmpeg/ffprobe detection
- regular video-to-frame ingest
- capture-policy generation
- FusionCapture mode metadata
- robotics sensor-log sync scaffold
- memory-tier docs
- hardware acceleration docs
- schema files for capture policy, sensor frames, and robotics sessions

Not complete yet:

- live camera/screen capture runtime
- hardware encoder selection engine
- native robot middleware integrations
- synchronized multi-camera ingestion
- native OmniBinary storage backend
- native Arc-RAR binary archive format
