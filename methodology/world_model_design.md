# Visual World Model Design

For this project, a visual world model is a compact predictor of the next latent visual state, not a full generative environment simulator.

Given pooled or spatial latent features `z_(t-k:t-1)`, predict `z_hat_t`. Train with temporally adjacent source-domain sequences using a normalized latent prediction loss (e.g., cosine distance or smooth L1). Evaluate residual `r_t = d(z_t, z_hat_t)` on in-domain validation and shifted streams.

Important controls:
- Compare against a non-temporal feature-distance detector.
- Use sequence-aware splits to avoid adjacent-frame leakage.
- Report whether prediction residual detects semantic changes, weather changes, camera changes, or merely motion novelty.
- A large residual may reflect a rare but valid event, not model failure.
