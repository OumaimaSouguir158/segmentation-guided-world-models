# Data Split Protocol

Create four disjoint partitions where dataset rules allow:
1. Source train: train encoder, segmentation head and temporal predictor.
2. Source validation: choose architecture and early stopping.
3. Calibration: estimate normalization constants, score weights and thresholds.
4. Shift test: final evaluation only.

For temporally correlated datasets, split by sequence/route/city rather than frame. Record exact official split names and any custom subset manifest. Keep a machine-readable manifest with image IDs, never private download credentials.
