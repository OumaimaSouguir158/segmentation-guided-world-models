# E3/E4 — Drift Detection

Shift families:
1. controlled image corruptions (brightness, contrast, blur, noise, weather-like effects);
2. ACDC adverse conditions;
3. cross-dataset/domain shift where class mappings are defensible;
4. temporal/sequence changes.

Calibrate on one set of conditions and evaluate on held-out conditions. Report AUROC, AUPR, FPR@95TPR, detection delay and false alarms. Include a no-drift in-domain stream to measure nuisance alarms.
