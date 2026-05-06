# ARC-StreamMemory

<p align="center">
  <strong>Local-first visual second brain for AI-readable video, screen, snapshot, robotics, and source-spine memory.</strong>
</p>

<p align="center">
  <a href="https://github.com/GareBear99/ARC-StreamMemory"><img alt="Repo" src="https://img.shields.io/badge/GitHub-ARC--StreamMemory-6d46ff?style=for-the-badge&logo=github"></a>
  <img alt="Version" src="https://img.shields.io/badge/version-2.1.1-ff4fbf?style=for-the-badge">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img alt="FFmpeg" src="https://img.shields.io/badge/FFmpeg-compatible-007808?style=for-the-badge&logo=ffmpeg&logoColor=white">
  <img alt="Local First" src="https://img.shields.io/badge/local--first-AI%20memory-111827?style=for-the-badge">
</p>

**ARC-StreamMemory** turns video files, screen recordings, screenshots, DAW/plugin sessions, game footage, browser work, robotics camera feeds, and app UI states into deterministic, cryptographically hashed, AI-readable visual memory modules.

It is designed as the **visual second brain / AI sight spine** for the GareBear99 ARC ecosystem: frames become indexed evidence, summaries become module attachments, hashes become source-spine proof, and capture sessions become replayable memory bundles.

---

## Quick answer

ARC-StreamMemory is for anyone searching for:

- AI visual memory
- visual second brain
- video memory for LLMs
- screen recording for AI
- local-first multimodal memory
- visual RAG / frame retrieval
- deterministic video archive
- cryptographic frame hashing
- robotics camera memory
- FFmpeg frame sampling for AI
- reproducible visual evidence bundles
- AI-readable screenshots and session replay

---

## What it does

```text
visual source
→ regular FFmpeg video/snapshot ingest
→ chosen AI frame-speed schedule
→ frame hashes
→ seeded source spine
→ OCR-ready/event-ready timeline
→ AI digest
→ ARC-Core-style receipts
→ OmniBinary-style chunk map
→ Arc-RAR-style bundle manifest
→ local source-spine viewer
→ AI module attachment JSON
```

The output is not just an MP4 or screenshots. It is a structured memory object that another AI can inspect, replay, cite, and attach to a module.

---

## Why this matters

Normal screen recording answers:

```text
What happened? Maybe watch the whole video again.
```

ARC-StreamMemory answers:

```text
What happened?
→ Read the AI digest.
→ Jump to event 000042.
→ Open frame_000042.
→ Verify the frame hash.
→ Follow the ARC receipt.
→ Follow the OmniBinary-style pointer.
→ Package/restore through the Arc-RAR-style bundle manifest.
```

That makes the memory **AI-readable, deterministic, replayable, and source-verifiable**.

---

## Current status

| Capability | Status | Notes |
|---|---:|---|
| Demo generated visual-memory session | ✅ complete | deterministic proof session |
| Snapshot folder ingest | ✅ complete | screenshots/images into AI memory |
| Regular FFmpeg video ingest | ✅ complete if FFmpeg is installed | sample MP4/MOV/MKV/WebM at chosen FPS |
| AI frame-speed policy | ✅ complete | 0.2, 0.5, 1, 2, 5, 10 FPS-style workflows |
| Frame hashing | ✅ complete | SHA-256 per frame |
| Memory spine hashing | ✅ complete | deterministic session root lineage |
| Seeded source spine | ✅ complete | replayable seed/hash lineage |
| AI digest | ✅ complete | Markdown + JSON digest |
| AI module attachment | ✅ complete | structured object for AI consumption |
| ARC-Core-style receipts | ✅ complete | export format ready |
| OmniBinary-style chunk map | ✅ complete | pointer format ready |
| Arc-RAR-style bundle manifest | ✅ complete | ZIP export today, Arc-RAR integration later |
| Local HTML viewer | ✅ complete | inspect frames, events, digest, JSON |
| ARC-FusionCapture adapter layer | ✅ complete as adapter/spec | robotics-ready capture policy + sensor sync scaffolding |
| Native live screen capture | 🚧 integration gate | not falsely claimed yet |
| Real OCR engine | 🚧 integration gate | placeholder/index format ready |
| Native OmniBinary persistence | 🚧 integration gate | export map ready |
| Native Arc-RAR packaging | 🚧 integration gate | manifest ready |

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

## Regular FFmpeg workflow

ARC-StreamMemory works with normal FFmpeg today.

```bash
python scripts/ffmpeg_probe.py
python scripts/ingest_video.py input.mp4 --fps 1 --out sessions/video_memory
python scripts/build_stream_memory.py sessions/video_memory --title "Video memory"
python scripts/hash_memory_spine.py sessions/video_memory
python scripts/build_seed_spine.py sessions/video_memory
python scripts/build_ai_digest.py sessions/video_memory
python scripts/validate_memory_bundle.py sessions/video_memory
```

Recommended AI frame rates:

| FPS | Use case |
|---:|---|
| 0.2 | long passive session memory |
| 0.5 | lightweight visual diary |
| 1 | general AI inspection default |
| 2 | UI debugging / GitHub / DAW flows |
| 5 | detailed interaction review |
| 10 | motion-sensitive review |

---

## ARC-FusionCapture compatibility

ARC-StreamMemory now includes a compatibility layer for the planned **ARC-FusionCapture** runtime.

**ARC-FusionCapture** is the future robotics/media capture layer that should wrap regular FFmpeg with:

- camera/feed profiles
- robotics capture modes
- hardware-acceleration selection
- sensor timestamp sync
- rolling buffer policy
- event-triggered clips
- AI-friendly frame-speed output
- ARC-Core receipts
- OmniBinary pointers
- Arc-RAR bundle manifests

Current files:

```text
integrations/arc_fusion_capture/README.md
integrations/arc_fusion_capture/profile_presets.json
scripts/build_capture_policy.py
scripts/fusion_capture_adapter.py
scripts/sync_sensor_log.py
schemas/capture_policy.schema.json
schemas/sensor_frame.schema.json
schemas/robotics_session.schema.json
```

Example robotics-style adapter flow:

```bash
python scripts/build_capture_policy.py --mode robot_navigation --fps 2 --out sessions/nav_test/memory/capture_policy.json
python scripts/fusion_capture_adapter.py --input robot_run.mp4 --policy sessions/nav_test/memory/capture_policy.json --out sessions/nav_test
python scripts/sync_sensor_log.py sessions/nav_test examples/sensor_log.jsonl
python scripts/build_stream_memory.py sessions/nav_test --title "Robot navigation memory"
python scripts/build_seed_spine.py sessions/nav_test
python scripts/validate_memory_bundle.py sessions/nav_test
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

## Seeded source-spine model

ARC-StreamMemory stores visual memory with a deterministic seed chain:

```text
capture_policy_hash
+ source_fingerprint
+ frame_schedule_hash
+ ordered_frame_hashes
+ chunk_hash
= session_root_seed
```

This gives the session a reproducible source spine:

```text
root_seed
→ chunk_000001
→ frame_000001
→ frame_hash
→ event_receipt
→ module_attachment_pointer
```

This pattern was strengthened using the seeded replay/source-lineage direction from [Seeded-Universe-Recreation-Engine](https://github.com/GareBear99/Seeded-Universe-Recreation-Engine).

---

## Ecosystem repo references

ARC-StreamMemory is part of a linked ARC / TizWildin / GareBear99 ecosystem. Every repo below is either a source reference, benchmark target, integration target, discovery surface, or public-router anchor.

| Repo | Role in ARC-StreamMemory |
|---|---|
| [ARC-Core](https://github.com/GareBear99/ARC-Core) | authority layer, receipts, event truth, source governance |
| [omnibinary-runtime](https://github.com/GareBear99/omnibinary-runtime) | binary-addressable memory spine and chunk-ledger inspiration |
| [Arc-RAR](https://github.com/GareBear99/Arc-RAR) | portable archive/restore bundle direction |
| [ARC-Neuron-LLMBuilder](https://github.com/GareBear99/ARC-Neuron-LLMBuilder) | local AI memory, governed build loop, module attachment use case |
| [ARC-AudioBench](https://github.com/GareBear99/ARC-AudioBench) | benchmark/evidence methodology companion |
| [Seeded-Universe-Recreation-Engine](https://github.com/GareBear99/Seeded-Universe-Recreation-Engine) | seeded source-spine / deterministic replay storage model |
| [FreeEQ8](https://github.com/GareBear99/FreeEQ8) | DAW/plugin testing screen-memory target |
| [FreeVox8](https://github.com/GareBear99/FreeVox8) | spectral plugin / visual-memory benchmark target |
| [Voxel Audio](https://github.com/GareBear99/Voxel_Audio) | audio-visual router/session target |
| [Instrudio](https://github.com/GareBear99/Instrudio) | Web Audio / MIDI / virtual instrument memory target |
| [awesome-audio-plugins-dev](https://github.com/GareBear99/awesome-audio-plugins-dev) | Start Here technical discovery list |
| [awesome-audio-lists](https://github.com/GareBear99/awesome-audio-lists) | root hub for audio/list/discovery resources |
| [awesome-python-audio-science](https://github.com/GareBear99/awesome-python-audio-science) | research/citation bridge for Python audio science, MIR, DSP, ML audio |
| [awesome-music-platforms](https://github.com/GareBear99/awesome-music-platforms) | artist/music platform discovery map |
| [TizWildinEntertainmentHUB](https://github.com/GareBear99/TizWildinEntertainmentHUB) | public router for plugins, lists, packs, deconstructed loops, visualizers |
| [TizWildin-Release-Vault](https://github.com/GareBear99/TizWildin-Release-Vault) | release surface for music assets, deconstructed loops, and packs |

---

## Public-facing use cases

### AI developer

Use ARC-StreamMemory to turn debugging videos and UI sessions into reproducible visual memory modules.

### Audio/plugin developer

Use it to archive DAW/plugin tests, FreeEQ8/FreeVox8 validation sessions, pluginval videos, and UI regressions.

### Robotics developer

Use regular FFmpeg now, then connect ARC-FusionCapture later for sensor-synced camera memory and robot black-box replay.

### Research / reproducibility

Use `CITATION.cff`, seeded spines, hashes, and module attachments to make visual sessions citable and reproducible.

### Creator / game developer

Use it to capture game states, UI flows, visual bugs, and build history as replayable evidence bundles.

---

## Recommended GitHub topics

```text
ai-memory
visual-memory
video-memory
screen-recording
multimodal-ai
visual-rag
local-first
ffmpeg
robotics
computer-vision
cryptographic-hashing
reproducible-research
second-brain
arc-core
omnibinary
arc-rar
```

---

## Honest completion status

This package is complete as a **public source release foundation** for deterministic visual memory:

- ingest
- indexing
- hashing
- seeded source-spine storage
- AI digest
- module attachment
- viewer
- validation
- regular FFmpeg workflow
- ARC-FusionCapture adapter layer
- bundle export

Remaining integration gates are intentionally not overclaimed:

- native live screen capture
- real OCR engine hookup
- native OmniBinary persistence
- native Arc-RAR packaging
- live ARC-Core API sync
- production robotics sensor bus integration

---

## License

MIT License.
