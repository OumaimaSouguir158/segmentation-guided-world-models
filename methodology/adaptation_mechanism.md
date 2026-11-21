# Test-Time Adaptation Mechanism

## Conservative controller
Adaptation is permitted only when:
1. the drift score exceeds a pre-calibrated threshold;
2. the current batch contains enough confident, non-ambiguous samples;
3. the update budget has not been exhausted;
4. a guard check does not indicate a collapse in prediction consistency.

Candidate update parameters, in order:
- normalization affine parameters/statistics;
- a small residual adapter;
- full-network parameters only as a costly exploratory ablation.

Candidate objective: entropy minimization on selected pixels plus temporal consistency regularization. Pseudo-labels must be confidence-filtered and class-balanced where possible.

## Safety mechanisms
- Keep immutable source checkpoint.
- Maintain a recent known-good adapted checkpoint.
- Limit gradient norm and update steps.
- Reject non-finite loss/parameters.
- Roll back if an unlabeled guard metric or consistency metric degrades sharply.
- Log every update decision and reason.

These safeguards reduce some risks but do not guarantee safe adaptation.
