from pathlib import Path
import sys, argparse
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path: sys.path.insert(0, str(ROOT_DIR))
from scripts.common import read_json, sha256_file, write_json, utc_now, list_frames
REQUIRED=['memory/capture_policy.json','memory/frame_index.json','memory/event_timeline.jsonl','memory/module_attachment.json','memory/memory_spine.json','memory/seed_spine.json','receipts/arc_receipts.jsonl','omnibinary/chunk_map.json','arcrar/bundle_manifest.json']
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('session'); args=ap.parse_args(); session=Path(args.session); errors=[]
    for rel in REQUIRED:
        if not (session/rel).exists(): errors.append(f'Missing {rel}')
    frames=list_frames(session)
    if not frames: errors.append('No frames found.')
    if (session/'memory/frame_index.json').exists():
        idx=read_json(session/'memory/frame_index.json')
        if len(idx.get('frames',[])) != len(frames): errors.append('Frame count mismatch.')
        for f in idx.get('frames',[]):
            p=session/f['path']
            if not p.exists(): errors.append(f"Missing frame {f['path']}")
            elif sha256_file(p) != f['sha256']: errors.append(f"Hash mismatch {f['path']}")
    write_json(session/'reports'/'validation_report.json', {'schema':'arc.streammemory.validation_report.v1','created_at':utc_now(),'ok':not errors,'errors':errors,'frame_files':len(frames)})
    if errors:
        print('\n'.join(errors)); raise SystemExit(1)
    print('Validation OK')
if __name__=='__main__': main()
