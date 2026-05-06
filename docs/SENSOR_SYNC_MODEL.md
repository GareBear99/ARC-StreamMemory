# Sensor Sync Model

Robotics sessions need visual frames connected to physical state.

ARC-StreamMemory v2.1.0 supports a sensor-log sync file:

```bash
python scripts/sync_sensor_log.py sessions/run_001 --sensor-log examples/sensor_log.jsonl
```

The sensor log is copied into:

```text
sensors/sensor_log.jsonl
memory/sensor_sync_index.json
```

## Sensor frame shape

```json
{
  "timestamp_ms": 1000,
  "frame_id": "frame_000002",
  "pose": {"x": 1.0, "y": 0.2, "z": 0.0, "yaw": 90.0},
  "robot_state": {"battery": 82, "mode": "inspection"}
}
```

v2.1.0 does nearest-timestamp matching. Future versions can support nanosecond clocks, IMU/camera calibration, and multi-camera sync.
