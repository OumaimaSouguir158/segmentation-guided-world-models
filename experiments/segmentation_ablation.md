# E4a — Segmentation-Signal Ablations

Compare:
- backbone feature distance only;
- semantic histogram divergence only;
- semantic confidence/entropy only;
- feature + semantic;
- all signals.

Use identical stream windows and calibration splits. Analyze classes with rare prevalence and scenes with genuine composition changes. A semantic histogram alarm may be caused by a different scene, not necessarily a harmful shift.
