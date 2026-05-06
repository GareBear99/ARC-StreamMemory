from pathlib import Path
import sys, json
ROOT=Path(__file__).resolve().parents[1]
REQUIRED=["README.md","QUICKSTART.md","CITATION.cff","docs/ARCHITECTURE.md","docs/SEEDED_VISUAL_MEMORY_STORAGE.md","docs/SOURCE_SPINE_REPLAY_MODEL.md","docs/AI_MODULE_ATTACHMENT.md","docs/VIEWER_DESIGN.md","docs/PRIVACY_AND_PERMISSIONS.md","scripts/create_demo_session.py","scripts/ingest_video.py","scripts/ingest_snapshot_folder.py","scripts/build_stream_memory.py","scripts/hash_memory_spine.py","scripts/build_seed_spine.py","scripts/build_ai_digest.py","scripts/verify_source_spine.py","scripts/validate_memory_bundle.py","scripts/make_bundle.py","viewer/index.html","viewer/viewer.js","viewer/style.css","schemas/module_attachment.schema.json","schemas/frame_index.schema.json","schemas/seed_spine.schema.json","examples/demo_session/memory/seed_spine.json","examples/demo_session/memory/ai_digest.md","data/repo_references.json"]
def main():
    errors=[]
    for rel in REQUIRED:
        if not (ROOT/rel).exists(): errors.append(f"Missing {rel}")
    for p in ROOT.rglob("*.json"):
        try: json.loads(p.read_text(encoding="utf-8"))
        except Exception as e: errors.append(f"Invalid JSON {p.relative_to(ROOT)}: {e}")
    readme=(ROOT/"README.md").read_text(encoding="utf-8")
    for term in ["AI visual memory","visual second brain","ARC-Core","OmniBinary","Arc-RAR","Seeded-Universe-Recreation-Engine","regular FFmpeg","ARC-FusionCapture","FreeEQ8","FreeVox8","awesome-python-audio-science"]:
        if term not in readme: errors.append(f"README missing {term}")
    if errors:
        print("Validation failed:"); print("\n".join("- "+e for e in errors)); raise SystemExit(1)
    print("Repository validation OK")
if __name__=="__main__": main()
