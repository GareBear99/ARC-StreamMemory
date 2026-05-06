from pathlib import Path
import sys
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path: sys.path.insert(0, str(ROOT_DIR))
import argparse, zipfile
from scripts.common import sha256_file, write_json, utc_now

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("session"); ap.add_argument("--out", required=True); args=ap.parse_args()
    session=Path(args.session); out=Path(args.out); out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED) as z:
        for p in session.rglob("*"):
            if p.is_file(): z.write(p,p.relative_to(session))
    write_json(session/"reports"/"bundle_export_report.json", {"schema":"arc.streammemory.bundle_export_report.v2","created_at":utc_now(),"bundle":str(out),"sha256":sha256_file(out)})
    print(out)
if __name__=="__main__": main()
