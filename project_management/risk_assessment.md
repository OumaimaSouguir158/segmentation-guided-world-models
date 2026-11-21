# Risk Register

| Risk | Likelihood/impact | Mitigation |
|---|---|---|
| GPU memory/time insufficient | Medium/high | Reduced resolution, compact model, staged experiments |
| Dataset access/license delay | Medium/medium | Start with one accessible dataset; document terms |
| Novelty overlap with recent work | Medium/high | Month-1 literature audit and scope revision |
| Sequence leakage | Medium/high | Sequence/city-level splits |
| Pseudo-label collapse | Medium/high | Confidence filtering, update budget, rollback |
| False drift alarms | High/medium | In-domain novelty tests and per-condition analysis |
| Unstable conclusions | Medium/high | Multiple seeds, intervals, pre-defined metrics |
| Incomplete implementation | Medium/medium | Go/no-go gates and scope prioritization |
