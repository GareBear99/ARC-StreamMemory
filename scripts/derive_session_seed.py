from pathlib import Path
import sys
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path: sys.path.insert(0, str(ROOT_DIR))
import argparse
from scripts.common import read_json

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("session"); args=ap.parse_args()
    print(read_json(Path(args.session)/"memory"/"seed_spine.json")["root_seed"])
if __name__=="__main__": main()
