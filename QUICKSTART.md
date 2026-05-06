# Quickstart

```bash
python3 scripts/create_demo_session.py
python3 scripts/build_stream_memory.py examples/demo_session --title "Demo visual memory"
python3 scripts/hash_memory_spine.py examples/demo_session
python3 scripts/build_seed_spine.py examples/demo_session
python3 scripts/validate_memory_bundle.py examples/demo_session
python3 scripts/make_bundle.py examples/demo_session --out release_evidence/demo_streammemory_bundle.zip
```
