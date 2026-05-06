from pathlib import Path
import sys, json
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path: sys.path.insert(0, str(ROOT_DIR))
REQUIRED=['README.md','QUICKSTART.md','CITATION.cff','docs/SEEDED_VISUAL_MEMORY_STORAGE.md','docs/SOURCE_SPINE_REPLAY_MODEL.md','scripts/build_seed_spine.py','scripts/derive_session_seed.py','schemas/seed_spine.schema.json','examples/demo_session/memory/seed_spine.json','data/repo_references.json']
def main():
    errors=[]
    for rel in REQUIRED:
        if not (ROOT_DIR/rel).exists(): errors.append(f'Missing {rel}')
    for p in ROOT_DIR.rglob('*.json'):
        try: json.loads(p.read_text(encoding='utf-8'))
        except Exception as e: errors.append(f'Invalid JSON {p.relative_to(ROOT_DIR)}: {e}')
    if errors:
        print('Validation failed:'); [print('-',e) for e in errors]; raise SystemExit(1)
    print('Repository validation OK')
if __name__=='__main__': main()
