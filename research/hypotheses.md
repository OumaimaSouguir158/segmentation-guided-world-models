# Hypotheses and Falsification Criteria

- H1: The fused detector exceeds the best single-signal detector on mean AUROC across held-out shift families. Falsified if it does not, within uncertainty.
- H2: Gated adaptation reduces the rate of severe performance regressions relative to always-on TTA. Falsified if regression frequency is not lower.
- H3: The gain persists across at least two distinct shift families. Falsified if improvements occur only on one selected condition.
- H4: Lightweight adaptation has lower latency and memory than full-network adaptation. This is a systems expectation to measure, not an accuracy claim.

Use at least three random seeds where feasible. Report confidence intervals and per-condition results; do not select thresholds using test labels.
