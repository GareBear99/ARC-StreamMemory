from pathlib import Path
import sys
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path: sys.path.insert(0, str(ROOT_DIR))
import argparse
from scripts.common import sha256_file, sha256_text, write_json, utc_now
FILES=["memory/frame_index.json","memory/event_timeline.jsonl","memory/ocr_index.jsonl","memory/module_attachment.json","receipts/arc_receipts.jsonl","omnibinary/chunk_map.json","arcrar/bundle_manifest.json"]
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("session"); args=ap.parse_args(); session=Path(args.session); entries=[]; concat=""
    for rel in FILES:
        p=session/rel
        if not p.exists(): raise SystemExit(f"Missing {rel}")
        h=sha256_file(p); entries.append({"path":rel,"sha256":h}); concat+=rel+h
    write_json(session/"memory"/"memory_spine.json", {"schema":"arc.streammemory.memory_spine.v2","created_at":utc_now(),"root_hash":sha256_text(concat),"entries":entries})
    print("Memory spine built")
if __name__=="__main__": main()
