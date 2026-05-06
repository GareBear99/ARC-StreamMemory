# Seeded Visual Memory Storage

ARC-StreamMemory v1.1.0 stores visual sessions through deterministic seeded source-spine metadata.

```text
capture_policy_hash + frame_schedule_hash + ordered_frame_hash + chunk_hash = root_seed
```

This gives AI memory a reproducible source spine rather than loose screenshots.
