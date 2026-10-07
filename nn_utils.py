import torch
import torch.nn as nn


class MLP(nn.Module):
    def __init__(self, d_in, h1=256, h2=64, p_in=0.2, p=0.5):
        super().__init__()
        self.net = nn.Sequential(
            nn.Dropout(p_in),
            nn.Linear(d_in, h1), nn.ReLU(), nn.Dropout(p),
            nn.Linear(h1, h2), nn.ReLU(), nn.Dropout(p),
            nn.Linear(h2, 1),
        )

    def forward(self, x):
        return self.net(x).squeeze(-1)
