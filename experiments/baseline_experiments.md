# E1 — Source-Only Segmentation Baseline

Train a standard segmentation architecture on the source training split. Establish mIoU and per-class IoU on source validation and in-domain calibration data. Freeze the checkpoint before target adaptation experiments. Record training time, throughput, memory, input resolution and seed. A baseline that cannot be reproduced blocks later claims.
