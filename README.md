# ARC-StreamMemory

**ARC-StreamMemory** is a local-first visual second brain for AI systems: video, screen recordings, screenshots, DAW/plugin sessions, game footage, browser work, terminal output, and app UI states become deterministic, cryptographically hashed, AI-readable memory modules.

It is designed for the GareBear99 / TizWildin / ARC ecosystem:

- **ARC-Core** — authority, receipts, and event truth
- **OmniBinary Runtime** — binary-addressable memory spine and chunk ledger
- **Arc-RAR** — portable archive / restore bundle
- **ARC-Neuron-LLMBuilder** — local AI memory and governed build loop
- **Seeded-Universe-Recreation-Engine** — deterministic seeded source-spine reference
- **ARC-AudioBench** — benchmark/evidence methodology companion
- **FreeEQ8 / FreeVox8 / Voxel Audio / Instrudio** — target sessions for plugin, visualizer, and instrument memory

---

## What it does

```text
visual source
→ video or snapshot ingest
→ chosen AI frame-speed schedule
→ frame hashes
→ seeded source spine
→ OCR-ready/event-ready timeline
→ AI digest
→ ARC receipts
→ OmniBinary-style chunk map
→ Arc-RAR-style bundle manifest
→ local source-spine viewer
→ AI module attachment JSON
```

---

## Modes

| Mode | Status | Purpose |
|---|---:|---|
| Demo generated frames | ✅ complete | deterministic proof session |
| Snapshot folder ingest | ✅ complete | turn screenshots/images into AI memory |
| Video frame ingest | ✅ complete if `ffmpeg` installed | sample video at chosen FPS |
| AI digest generation | ✅ complete | AI-readable summary with frame/event refs |
| Seeded source spine | ✅ complete | root seed, schedule hash, chunk hash, frame hash lineage |
| Local viewer | ✅ complete | inspect frames, digest, events, hashes, attachment |
| ARC-Core integration | ✅ export/client scaffold | push receipts/module metadata later |
| OmniBinary integration | ✅ export/client scaffold | write/read chunk maps later |
| Arc-RAR integration | ✅ export/client scaffold | native bundle adapter later |
| Live screen recording | 🚧 integration gate | documented next step |
| OCR engine | 🚧 integration gate | placeholder/index format ready |
| Privacy redaction | 🚧 integration gate | policy + redaction log format ready |

---

## Quickstart

```bash
python scripts/create_demo_session.py
python scripts/build_stream_memory.py examples/demo_session --title "ARC demo visual memory"
python scripts/hash_memory_spine.py examples/demo_session
python scripts/build_seed_spine.py examples/demo_session
python scripts/build_ai_digest.py examples/demo_session
python scripts/validate_memory_bundle.py examples/demo_session
python scripts/make_bundle.py examples/demo_session --out release_evidence/demo_streammemory_bundle.zip
```

Open viewer:

```bash
python -m http.server 8080
```

Then open:

```text
http://localhost:8080/viewer/index.html?session=../examples/demo_session/memory/module_attachment.json
```

---

## Video ingest

```bash
python scripts/ingest_video.py input.mp4 --fps 1 --out sessions/video_memory
python scripts/build_stream_memory.py sessions/video_memory --title "Video memory"
python scripts/build_seed_spine.py sessions/video_memory
python scripts/build_ai_digest.py sessions/video_memory
python scripts/validate_memory_bundle.py sessions/video_memory
```

Requires `ffmpeg` on PATH.

---

## Snapshot folder ingest

```bash
python scripts/ingest_snapshot_folder.py ./screenshots --out sessions/snapshot_memory
python scripts/build_stream_memory.py sessions/snapshot_memory --title "Snapshot memory"
python scripts/build_seed_spine.py sessions/snapshot_memory
python scripts/build_ai_digest.py sessions/snapshot_memory
python scripts/validate_memory_bundle.py sessions/snapshot_memory
```

---

## Output structure

```text
session/
├─ frames/
├─ memory/
│  ├─ capture_policy.json
│  ├─ frame_index.json
│  ├─ event_timeline.jsonl
│  ├─ ocr_index.jsonl
│  ├─ ai_digest.md
│  ├─ ai_digest.json
│  ├─ module_attachment.json
│  ├─ memory_spine.json
│  ├─ seed_spine.json
│  └─ session_summary.md
├─ receipts/arc_receipts.jsonl
├─ omnibinary/chunk_map.json
├─ arcrar/bundle_manifest.json
├─ reports/validation_report.json
└─ reports/bundle_export_report.json
```

---

## SEO positioning

**ARC-StreamMemory** targets: AI visual memory, visual second brain, video memory for LLMs, screen recording for AI, local-first AI memory, visual RAG, deterministic visual memory, seeded source spine, cryptographic video archive, multimodal memory, frame sampling for AI, AI module attachments, and reproducible screen memory.

---

## Honest completion status

This package is complete as a **public source release foundation** for deterministic visual memory: ingest, indexing, hashing, seeded spine storage, AI digest, module attachment, viewer, validation, and bundle export.

Remaining integration gates are clearly separated: native live capture, OCR engine hookup, native OmniBinary persistence, native Arc-RAR packaging, and live ARC-Core API sync.
