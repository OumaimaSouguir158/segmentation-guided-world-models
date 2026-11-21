# three-Month Research Execution Plan

| Month | Work | Deliverable / exit criterion |
|---|---|---|
| 1 | Literature review; confirm novelty; dataset access; environment and split design | Annotated bibliography, final scope, data manifest, baseline protocol |
| 2 | Implement and validate source segmentation baseline; establish metrics | Reproducible source checkpoint and baseline report |
| 3 | Implement latent predictor and three drift signals; calibrate on held-out validation | Drift detector prototype and signal ablation report |
| 4 | Implement fused score; evaluate adverse/cross-domain shifts; analyze false alarms | Detection benchmark with per-condition results |
| 5 | Implement gated TTA and compatible published baselines; run stability/efficiency tests | Adaptation comparison, rollback logs, compute report |
| 6 | Statistical analysis, failure analysis, documentation and writing | Final report, clean code release, reproducibility package; manuscript only if evidence supports it |

## Go/no-go gates
- End M1: dataset terms and a feasible dataset pair confirmed.
- End M2: baseline pipeline reproduces metrics on a fixed split.
- End M3: drift signals run end-to-end and can be calibrated without test leakage.
- End M4: detection results include false-alarm analysis.
- End M5: adaptation comparison includes rollback and negative outcomes.
- End M6: every reported claim traceable to an artifact.

## Scope control
If compute is limited, prioritize Cityscapes/ACDC, one compact segmentation model, one temporal predictor, and core ablations. Defer multi-dataset expansion rather than weakening reproducibility.
