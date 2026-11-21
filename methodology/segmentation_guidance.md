# Segmentation Guidance

The segmentation branch provides two kinds of information:

1. **Per-pixel uncertainty:** entropy of the class probability vector. Aggregate using robust summaries (median, upper quantile), not only the mean.
2. **Semantic composition:** normalized class histogram over valid pixels. Compare current-window histogram with a source reference using Jensen–Shannon divergence. Because class prevalence legitimately varies by location, composition shift is a warning signal, not proof of failure.

Optional later ablation: spatially pooled class maps or class-conditional feature prototypes. Do not add these until the simpler protocol is established.
