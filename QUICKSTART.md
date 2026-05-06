# Quickstart

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
