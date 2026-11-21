# Limitations

1. Semantic histogram shift can reflect legitimate scene composition changes.
2. Prediction residual can respond to rare but valid events, camera cuts or motion.
3. Entropy minimization can amplify confident errors.
4. A drift detector calibrated on known shifts may fail on unseen shifts.
5. Cityscapes/ACDC do not represent every geography, camera or application.
6. Results from offline replay may not transfer to real-time deployment.
7. A compact latent predictor is only one operationalization of a visual world model.
8. Compute constraints may limit model scale and statistical power.

These limitations must be revisited after experiments.
