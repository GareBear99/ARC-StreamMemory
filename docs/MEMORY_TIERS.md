# Memory Tiers

Robotics visual memory must avoid storing everything forever.

| Tier | Stored data | Use |
|---|---|---|
| 0 | live frame only | realtime control |
| 1 | keyframes + hashes | default AI memory |
| 2 | event clips + keyframes | debugging |
| 3 | compressed session video | review/archive |
| 4 | raw full recording | opt-in evidence/training |

ARC-StreamMemory defaults to tier 1/2-style storage: keyframes, hashes, receipts, digest, and bundle metadata.
