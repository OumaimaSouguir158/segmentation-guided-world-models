# Evaluation Protocol

## Split discipline
- Split by sequence, city, or source video wherever possible; never randomly split adjacent frames across train and test.
- Source training data, in-domain calibration data, shifted validation data, and final shifted test data must be distinct.
- Drift labels and target semantic labels are evaluator-only.
- Select thresholds/weights on validation conditions; reserve test conditions for final reporting.

## Metrics
**Segmentation:** mIoU, per-class IoU, pixel accuracy, mean class accuracy.  
**Drift:** AUROC, AUPR, FPR@95TPR, detection delay, false alarms/hour or per sequence.  
**Reliability:** ECE with documented binning, Brier score, predictive entropy.  
**Adaptation:** target mIoU change vs source-only, recovery after shift, regression frequency, forgetting on return to source.  
**Efficiency:** throughput, per-frame latency, peak GPU memory, trainable parameter count, update frequency.

## Statistical reporting
Use multiple seeds where feasible; report mean and standard deviation or bootstrap confidence intervals. Show per-shift-family tables. Do not aggregate away catastrophic regressions.
