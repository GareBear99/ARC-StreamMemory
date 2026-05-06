from pathlib import Path
import sys, json
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path: sys.path.insert(0, str(ROOT_DIR))
import argparse
from scripts.common import read_json, write_json, utc_now, sha256_text

def read_jsonl(path):
    if not path.exists(): return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("session"); args=ap.parse_args(); session=Path(args.session)
    attach=read_json(session/"memory"/"module_attachment.json"); frame_index=read_json(session/"memory"/"frame_index.json"); events=read_jsonl(session/"memory"/"event_timeline.jsonl")
    keyframes=[e.get("frame_ref") for e in events if e.get("frame_ref")]
    md=[f"# AI Digest — {attach['title']}","",attach.get("summary", ""),"",f"Session ID: `{attach['session_id']}`",f"Frame count: **{frame_index['frame_count']}**",f"Capture mode: `{attach.get('capture_policy',{}).get('capture_mode','unknown')}`","","## Key Events"]
    for e in events: md.append(f"- `{e.get('time_ms',0)}ms` — **{e.get('type')}** — {e.get('summary')} (`{e.get('frame_ref')}`)")
    if not events: md.append("- No events recorded yet.")
    md.append("\n## Recommended AI Use\nRead this digest first, then inspect exact frames by frame_id/hash when more evidence is needed.\n")
    digest_md="\n".join(md)
    (session/"memory"/"ai_digest.md").write_text(digest_md, encoding="utf-8")
    digest_json={"schema":"arc.streammemory.ai_digest.v1","created_at":utc_now(),"session_id":attach["session_id"],"title":attach["title"],"frame_count":frame_index["frame_count"],"event_count":len(events),"keyframes":keyframes,"digest_hash":sha256_text(digest_md)}
    write_json(session/"memory"/"ai_digest.json", digest_json)
    print("AI digest built")
if __name__=="__main__": main()
