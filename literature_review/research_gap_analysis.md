# Preliminary Research-Gap Analysis

| Existing line | Typical signal / objective | Limitation relevant to this project | Proposed test |
|---|---|---|---|
| Feature-statistics OOD/drift monitoring | Feature distances, confidence, density | May not reveal whether scene semantics or temporal expectations changed | Compare against semantic and predictive signals |
| Semantic segmentation domain adaptation | Align features or output distributions across domains | Often assumes a known target domain or adaptation training phase | Evaluate online unlabeled stream adaptation |
| Entropy-minimization TTA | Reduce prediction entropy online | Can reinforce confident errors and drift over time | Add conservative gate, confidence and rollback |
| Continual TTA | Memory, teacher/student, sample selection | More machinery and update cost; failure under non-stationarity remains possible | Measure stability and resource costs |
| Latent world models | Predict latent future states | Usually optimized for representation/planning, not calibrated perception drift alarms | Test prediction residual as a drift signal |
| Uncertainty/calibration | Confidence and predictive uncertainty | Uncertainty alone may be poorly calibrated under shift | Evaluate calibration and detection complementarity |

## Working gap
A rigorous comparison of **semantic distribution change**, **latent predictive surprise**, and **feature distribution shift** as complementary signals for drift detection, followed by a controlled evaluation of whether their fusion can safely gate lightweight segmentation TTA.

## Must-do novelty verification
Search 2024–2026 proceedings and preprints for segmentation-aware TTA, temporal consistency under shift, predictive-error OOD detection, and world-model-based monitoring. The project must narrow or revise the novelty claim if a substantially similar method exists.
