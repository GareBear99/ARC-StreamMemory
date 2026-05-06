# ARC-StreamMemory

**ARC-StreamMemory** is a local-first visual second brain for AI systems.

It converts video, screen recordings, DAW/plugin captures, app footage, and image snapshots into reproducible visual memory: sampled frames, hashes, source-spine metadata, ARC-style receipts, OmniBinary-style chunk maps, Arc-RAR-style bundle manifests, and AI module attachments.

## v1.1.0 seeded source-spine model

This package adds seeded visual-memory storage inspired by the Seeded-Universe-Recreation-Engine source-spine model:

```text
root seed
→ capture policy
→ source fingerprint
→ deterministic frame schedule
→ ordered frame hashes
→ chunk hashes
→ session root hash
→ OmniBinary-style spine pointer
→ Arc-RAR-style bundle manifest
→ ARC-Core-style receipts
```

## Quickstart

```bash
python3 scripts/create_demo_session.py
python3 scripts/build_stream_memory.py examples/demo_session --title "Demo visual memory"
python3 scripts/hash_memory_spine.py examples/demo_session
python3 scripts/build_seed_spine.py examples/demo_session
python3 scripts/validate_memory_bundle.py examples/demo_session
python3 scripts/make_bundle.py examples/demo_session --out release_evidence/demo_streammemory_bundle.zip
```

Open viewer:

```bash
python3 -m http.server 8080
```

Then open:

```text
http://localhost:8080/viewer/index.html?session=../examples/demo_session/memory/module_attachment.json
```

## Ecosystem references

- [ARC-Core](https://github.com/GareBear99/ARC-Core) — authority/receipt layer
- [omnibinary-runtime](https://github.com/GareBear99/omnibinary-runtime) — binary memory/source-spine reference
- [Arc-RAR](https://github.com/GareBear99/Arc-RAR) — portable archive/evidence bundle reference
- [ARC-Neuron-LLMBuilder](https://github.com/GareBear99/ARC-Neuron-LLMBuilder) — local AI memory/build governance reference
- [ARC-AudioBench](https://github.com/GareBear99/ARC-AudioBench) — benchmark/evidence methodology companion
- [Seeded-Universe-Recreation-Engine](https://github.com/GareBear99/Seeded-Universe-Recreation-Engine) — seeded replay/source-spine storage reference
- [FreeEQ8](https://github.com/GareBear99/FreeEQ8) — DAW/plugin visual-memory target
- [FreeVox8](https://github.com/GareBear99/FreeVox8) — spectral plugin visual-memory target
- [Voxel Audio](https://github.com/GareBear99/Voxel_Audio) — visual/audio routing reference
- [awesome-audio-plugins-dev](https://github.com/GareBear99/awesome-audio-plugins-dev) — Start Here technical list
- [awesome-python-audio-science](https://github.com/GareBear99/awesome-python-audio-science) — research/citation bridge

## Honest status

Complete public source package for deterministic visual-memory session generation, indexing, seeded spine storage, validation, viewer output, and bundle export.

Next integration gates: live screen capture, OCR, native Arc-RAR packaging, and full OmniBinary runtime ingestion.
