# Overall Framework

## Data flow
A temporally ordered image stream `x_t` is passed through a visual encoder `E`. The encoder produces latent representation `z_t`. A segmentation head `S` produces pixel-level class probabilities `p_t`. A temporal predictor `F` predicts the next latent representation from a context window: `z_hat_t = F(z_{t-k:t-1})`. The drift monitor compares current observations with a source reference and with the model's own temporal prediction. An adaptation controller decides whether to update a restricted parameter subset.

## Modules
1. **Encoder:** ResNet-50 or SegFormer MiT-B0/B1 initially; choose one reproducible baseline.
2. **Segmentation head:** standard decoder producing class logits.
3. **Latent predictor:** lightweight GRU/MLP or temporal transformer over pooled/spatial latent features.
4. **Drift monitor:** feature distance, semantic histogram divergence, predictive residual.
5. **Adaptation controller:** confidence gate, drift threshold, update budget, rollback.
6. **Evaluator:** offline-only ground-truth metrics and drift labels.

## Design principle
Detection and adaptation are evaluated separately. A detector can be useful even if adaptation does not improve segmentation; adaptation is not allowed to access ground-truth drift labels or target annotations.
