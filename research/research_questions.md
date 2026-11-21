# Research Questions and Operational Definitions

| ID | Question | Operational test |
|---|---|---|
| Q1 | Do semantic statistics add information to drift detection? | Compare semantic-only and feature-only detectors with fused detector on held-out shifts. |
| Q2 | Does latent prediction surprise help? | Compare prediction residual against semantic and feature signals, including temporally ordered streams. |
| Q3 | Does fusion generalize across shift families? | Train/choose thresholds on designated validation shifts; evaluate on held-out corruption/weather/domain shifts. |
| Q4 | Does gated adaptation reduce harmful updates? | Compare source-only, always-on TTA and gated TTA under identical streams and update budgets. |
| Q5 | Is the method computationally practical? | Measure wall-clock latency, peak GPU memory, trainable parameter count and updates per sample. |

**Drift label:** An evaluation-only indicator derived from known dataset/domain/condition changes. It must never be exposed to the online adaptation module.
