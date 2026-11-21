# System Architecture

```mermaid
flowchart LR
  A[Ordered image stream x(t)] --> B[Visual encoder E]
  B --> C[Latent feature z(t)]
  B --> D[Segmentation head S]
  D --> E[Pixel probabilities p(t)]
  C --> F[Temporal latent predictor F]
  F --> G[Prediction residual]
  C --> H[Feature drift monitor]
  E --> I[Semantic drift monitor]
  G --> J[Predictive drift monitor]
  H --> K[Score normalization and fusion]
  I --> K
  J --> K
  K --> L[Confidence and drift gate]
  L -->|safe update| M[Lightweight TTA adapter]
  L -->|reject update| N[Keep current parameters]
  M --> O[Updated perception model]
  N --> O
  O --> P[Predictions and audit log]
```

## Information boundaries
- Target labels are available only to the offline evaluator.
- Drift labels are available only to the offline evaluator.
- The online monitor receives images, model outputs, internal features, and source reference statistics.
- The adaptation controller cannot inspect test-set labels or future frames.
