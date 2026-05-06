# Robotics Capture Modes

ARC-FusionCapture-compatible modes:

| Mode | AI FPS | Retention | Use |
|---|---:|---|---|
| `navigation` | 1-2 | keyframes + events | robot navigation memory |
| `inspection` | 2-5 | keyframes + event clips | defects, objects, UI/field review |
| `blackbox` | 1 | rolling/event retention | failure analysis |
| `training` | 5-10 | full session optional | dataset creation |
| `snapshot` | manual | images only | low-weight visual state capture |

Each mode is written into `memory/capture_policy.json` and mirrored into `memory/module_attachment.json`.
