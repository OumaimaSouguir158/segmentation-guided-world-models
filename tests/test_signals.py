import torch
from src.drift_detection.signals import semantic_histogram, js_divergence, prediction_residual, fuse_scores

def test_histogram_sums_to_one():
    p = torch.softmax(torch.randn(2, 4, 8, 8), dim=1)
    h = semantic_histogram(p)
    assert torch.allclose(h.sum(1), torch.ones(2), atol=1e-5)

def test_js_same_distribution_zero():
    p = torch.tensor([[0.2, 0.8]])
    assert torch.allclose(js_divergence(p, p), torch.zeros(1), atol=1e-6)

def test_prediction_residual_identical_zero():
    x = torch.randn(3, 16)
    assert torch.allclose(prediction_residual(x, x), torch.zeros(3), atol=1e-6)

def test_fusion():
    x = torch.ones(2)
    assert torch.allclose(fuse_scores(x, x, x, x), x)
