# Technical Documentation

## Software
Python 3.10+ recommended; PyTorch 2.2+; see `requirements.txt`.

## Modules
- `src/drift_detection/signals.py`: semantic histograms, JS divergence, latent residual and score fusion.
- `src/world_models/latent_predictor.py`: GRU latent next-state predictor.
- `src/adaptation/gating.py`: threshold/confidence/budget gate.
- `src/evaluation/metrics.py`: confusion matrix and mIoU helper.

## Important status
These modules are a starting scaffold, not a complete training pipeline or validated research implementation. Dataset loaders, segmentation model integration, calibration, stream runner, optimizer/rollback and benchmark adapters remain implementation tasks described in the plan.
