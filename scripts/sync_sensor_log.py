#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, shutil, bisect, datetime
from pathlib import Path


def load_jsonl(path: Path):
    rows=[]
    with path.open('r', encoding='utf-8') as f:
        for line in f:
            line=line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def main():
    ap=argparse.ArgumentParser(description='Attach robotics/sensor log to an ARC-StreamMemory session.')
    ap.add_argument('session')
    ap.add_argument('--sensor-log', required=True, help='JSONL sensor log with timestamp_ms fields')
    args=ap.parse_args()
    session=Path(args.session); sensor=Path(args.sensor_log)
    if not sensor.exists():
        raise SystemExit(f'sensor log not found: {sensor}')
    sensors=load_jsonl(sensor)
    frame_index=json.loads((session/'memory'/'frame_index.json').read_text(encoding='utf-8'))
    sensor_times=[float(s.get('timestamp_ms',0)) for s in sensors]
    sync=[]
    for f in frame_index.get('frames',[]):
        t=float(f.get('timestamp_ms',0))
        if not sensors:
            nearest=None
        else:
            i=bisect.bisect_left(sensor_times,t)
            candidates=[]
            if i < len(sensors): candidates.append((abs(sensor_times[i]-t), sensors[i]))
            if i > 0: candidates.append((abs(sensor_times[i-1]-t), sensors[i-1]))
            nearest=sorted(candidates, key=lambda x:x[0])[0][1] if candidates else None
        sync.append({'frame_id':f['frame_id'],'frame_timestamp_ms':t,'sensor':nearest})
    out_dir=session/'sensors'; out_dir.mkdir(parents=True, exist_ok=True); shutil.copy2(sensor,out_dir/'sensor_log.jsonl')
    out={'schema':'arc.fusion_capture.sensor_sync.v1','created_at':datetime.datetime.now(datetime.UTC).replace(microsecond=0).isoformat(),'sensor_log':'sensors/sensor_log.jsonl','matches':sync}
    p=session/'memory'/'sensor_sync_index.json'; p.write_text(json.dumps(out,indent=2)+'
', encoding='utf-8')
    print(p)

if __name__=='__main__':
    main()
