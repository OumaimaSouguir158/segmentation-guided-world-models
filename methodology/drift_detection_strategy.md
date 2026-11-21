# Drift Detection Strategy

Let:
- `d_f(t)` be a feature-distribution distance (e.g., diagonal Mahalanobis distance or MMD) between a rolling target window and source reference features.
- `d_s(t)` be Jensen–Shannon divergence between semantic class histograms.
- `d_p(t)` be normalized latent prediction residual.
- `u(t)` be a segmentation uncertainty statistic.

Normalize each signal using robust statistics on a designated in-domain validation set: `q_i = clip((d_i - median_i)/(MAD_i + eps), 0, q_max)`. Choose scaling and thresholds without using final test labels.

A simple fused score is:
`D(t) = w_f q_f(t) + w_s q_s(t) + w_p q_p(t) + w_u q_u(t)`, where non-negative weights sum to one.

Compare:
- each signal independently;
- equal-weight fusion;
- validation-tuned fusion;
- logistic fusion trained only on a separate calibration split (if allowed by protocol).

Use AUROC, AUPR, FPR@95TPR, detection delay, and false alarms per stream. Evaluate on unseen shift families to assess generalization.
