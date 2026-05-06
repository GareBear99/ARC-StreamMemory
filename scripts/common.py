from pathlib import Path
import hashlib, json, datetime

def utc_now():
    return datetime.datetime.now(datetime.UTC).replace(microsecond=0).isoformat()

def sha256_file(path: Path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return "sha256:" + h.hexdigest()

def sha256_text(text: str):
    return "sha256:" + hashlib.sha256(text.encode("utf-8")).hexdigest()

def write_json(path: Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def append_jsonl(path: Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(obj, ensure_ascii=False) + "\n")

def list_frames(session_dir: Path):
    return sorted((session_dir / "frames").glob("frame_*.png"))
