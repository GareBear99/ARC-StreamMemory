from pathlib import Path
import sys, argparse
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path: sys.path.insert(0, str(ROOT_DIR))
from scripts.common import read_json, write_json, sha256_file, sha256_text, utc_now

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('session'); args=ap.parse_args(); session=Path(args.session)
    frame_index=read_json(session/'memory'/'frame_index.json'); chunk_map=read_json(session/'omnibinary'/'chunk_map.json')
    policy_hash=sha256_file(session/'memory'/'capture_policy.json')
    frame_hashes=[f['sha256'] for f in frame_index['frames']]
    frame_schedule=[f"{f['frame_id']}@{f['timestamp_ms']}" for f in frame_index['frames']]
    frame_schedule_hash=sha256_text('|'.join(frame_schedule)); ordered_frame_hash=sha256_text('|'.join(frame_hashes)); chunk_hash=sha256_text('|'.join(c['hash'] for c in chunk_map['chunks']))
    root_seed=sha256_text(policy_hash+frame_schedule_hash+ordered_frame_hash+chunk_hash)
    write_json(session/'memory'/'seed_spine.json', {'schema':'arc.streammemory.seed_spine.v1','created_at':utc_now(),'session_id':frame_index['session_id'],'root_seed':root_seed,'policy_hash':policy_hash,'frame_schedule_hash':frame_schedule_hash,'ordered_frame_hash':ordered_frame_hash,'chunk_hash':chunk_hash,'deterministic_replay':{'frame_count':frame_index['frame_count'],'frame_order':[f['frame_id'] for f in frame_index['frames']],'timestamps_ms':[f['timestamp_ms'] for f in frame_index['frames']]},'source_spine':{'arc_core_receipts':'receipts/arc_receipts.jsonl','omnibinary_chunk_map':'omnibinary/chunk_map.json','arcrar_bundle_manifest':'arcrar/bundle_manifest.json','module_attachment':'memory/module_attachment.json'}})
    print(root_seed)
if __name__=='__main__': main()
