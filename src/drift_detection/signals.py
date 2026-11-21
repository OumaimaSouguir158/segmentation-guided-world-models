"""Drift signal primitives. These are research utilities, not validated detectors."""
import torch

def prediction_residual(current: torch.Tensor, predicted: torch.Tensor) -> torch.Tensor:
    """Per-sample cosine residual for latent tensors [B, ...]."""
    a = current.flatten(1)
    b = predicted.flatten(1)
    return 1.0 - torch.nn.functional.cosine_similarity(a, b, dim=1)

def semantic_histogram(probabilities: torch.Tensor, eps: float = 1e-8) -> torch.Tensor:
    """Mean predicted class probabilities [B,C,H,W] -> normalized [B,C]."""
    if probabilities.ndim != 4:
        raise ValueError("Expected [B,C,H,W] probabilities")
    hist = probabilities.mean(dim=(-2, -1))
    return hist / hist.sum(dim=1, keepdim=True).clamp_min(eps)

def js_divergence(p: torch.Tensor, q: torch.Tensor, eps: float = 1e-8) -> torch.Tensor:
    """Jensen-Shannon divergence for normalized distributions [B,C]."""
    p = p.clamp_min(eps); q = q.clamp_min(eps)
    p = p / p.sum(dim=1, keepdim=True)
    q = q / q.sum(dim=1, keepdim=True)
    m = 0.5 * (p + q)
    kl_pm = (p * (p.log() - m.log())).sum(dim=1)
    kl_qm = (q * (q.log() - m.log())).sum(dim=1)
    return 0.5 * (kl_pm + kl_qm)

def fuse_scores(feature, semantic, predictive, uncertainty, weights=(0.25,0.25,0.25,0.25)):
    """Fuse already normalized 1-D score tensors; weights must sum to one."""
    if len(weights) != 4 or abs(sum(weights) - 1.0) > 1e-6:
        raise ValueError("weights must contain four values summing to one")
    return sum(float(w) * s for w, s in zip(weights, (feature, semantic, predictive, uncertainty)))
