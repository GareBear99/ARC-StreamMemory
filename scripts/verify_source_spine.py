from pathlib import Path
import sys
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path: sys.path.insert(0, str(ROOT_DIR))
import argparse, subprocess

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("session"); args=ap.parse_args()
    for script in ["hash_memory_spine.py", "build_seed_spine.py", "validate_memory_bundle.py"]:
        subprocess.run([sys.executable, str(ROOT_DIR/"scripts"/script), args.session], check=True)
    print("Source spine verified")
if __name__=="__main__": main()
