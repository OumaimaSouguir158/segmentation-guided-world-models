"""Minimal temporal latent predictor scaffold."""
import torch
from torch import nn

class LatentGRUPredictor(nn.Module):
    """Predict next pooled latent vector from a sequence [B,T,D]."""
    def __init__(self, latent_dim: int, hidden_dim: int = 256):
        super().__init__()
        self.gru = nn.GRU(latent_dim, hidden_dim, batch_first=True)
        self.head = nn.Sequential(nn.Linear(hidden_dim, hidden_dim), nn.GELU(),
                                  nn.Linear(hidden_dim, latent_dim))

    def forward(self, sequence: torch.Tensor) -> torch.Tensor:
        if sequence.ndim != 3:
            raise ValueError("Expected [B,T,D] latent sequence")
        _, h = self.gru(sequence)
        return self.head(h[-1])
