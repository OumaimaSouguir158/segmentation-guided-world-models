# Compute Plan

## Conservative starting point
Begin with a small subset and 512×1024 or lower input resolution, batch size 1–2, mixed precision where supported, gradient accumulation if needed, and a compact encoder/decoder. Profile memory before full training. The values in `configs/training.yaml` are initial placeholders for a feasibility run, not guaranteed optimal settings.

## Resource tiers
- CPU-only: data validation, literature work, small unit tests and toy models; not recommended for full segmentation training.
- Modest GPU (e.g., 8–12 GB): reduced resolution, small batch, frozen/compact encoder, short sequences, gradient accumulation.
- Larger GPU: increase resolution/batch only after profiling; report exact hardware.

Use free notebook GPUs only if terms, quotas and session persistence permit. Do not assume uninterrupted free compute. Store checkpoints externally and track disk usage.
