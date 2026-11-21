# Experiment Plan

All experiments below are planned. No result should be entered until code, data manifest, configuration and logs exist.

## Experiment sequence
E0: environment and data integrity checks.  
E1: source-only segmentation baseline.  
E2: in-domain calibration and corruption/adverse-condition evaluation.  
E3: feature-only, semantic-only and prediction-only drift detection.  
E4: fused drift detector and ablations.  
E5: source-only vs TENT/CoTTA/EATA/SAR/RoTTA-compatible baselines.  
E6: proposed gated adaptation.  
E7: efficiency, sensitivity, return-to-source and failure analysis.

## Minimum reproducibility record
Dataset/version, official/custom split, sequence IDs, model, config hash, code commit, random seed, hardware, software versions, checkpoint, metrics and log path.
