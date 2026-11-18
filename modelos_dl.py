"""MLP e BrainNetCNN para conectividade funcional no ADHD-200 (190 ROIs)."""
import torch
from torch import nn


class MLPConectividade(nn.Module):
    """MLP 17.955 -> 128 -> 64 -> 1, inspirado no notebook ABIDE de referência."""
    def __init__(self, n_atributos, dropout1=0.50, dropout2=0.40):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(n_atributos, 128), nn.ReLU(), nn.Dropout(dropout1),
            nn.Linear(128, 64), nn.ReLU(), nn.Dropout(dropout2),
            nn.Linear(64, 1),
        )

    def forward(self, x):
        return self.net(x).squeeze(1)


class E2E(nn.Module):
    """Edge-to-Edge: soma projeções aprendidas ao longo das linhas e colunas."""
    def __init__(self, n_rois, in_ch, out_ch):
        super().__init__()
        self.row_weight = nn.Parameter(torch.empty(out_ch, in_ch, n_rois))
        self.col_weight = nn.Parameter(torch.empty(out_ch, in_ch, n_rois))
        self.row_bias = nn.Parameter(torch.zeros(out_ch))
        self.col_bias = nn.Parameter(torch.zeros(out_ch))
        nn.init.xavier_uniform_(self.row_weight)
        nn.init.xavier_uniform_(self.col_weight)

    def forward(self, x):
        row = torch.einsum('bcij,fcj->bfi', x, self.row_weight)
        row = row + self.row_bias[None, :, None]
        col = torch.einsum('bcij,fci->bfj', x, self.col_weight)
        col = col + self.col_bias[None, :, None]
        return row.unsqueeze(-1) + col.unsqueeze(-2)


class E2N(nn.Module):
    """Edge-to-Node: agrega as conexões incidentes em cada ROI."""
    def __init__(self, n_rois, in_ch, out_ch):
        super().__init__()
        self.row_weight = nn.Parameter(torch.empty(out_ch, in_ch, n_rois))
        self.col_weight = nn.Parameter(torch.empty(out_ch, in_ch, n_rois))
        self.row_bias = nn.Parameter(torch.zeros(out_ch))
        self.col_bias = nn.Parameter(torch.zeros(out_ch))
        nn.init.xavier_uniform_(self.row_weight)
        nn.init.xavier_uniform_(self.col_weight)

    def forward(self, x):
        row = torch.einsum('bcij,fcj->bfi', x, self.row_weight)
        row = row + self.row_bias[None, :, None]
        col = torch.einsum('bcij,fci->bfj', x, self.col_weight)
        col = col + self.col_bias[None, :, None]
        return (row + col).unsqueeze(-1)


class N2G(nn.Module):
    """Node-to-Graph: transforma representações de ROI em vetor do participante."""
    def __init__(self, n_rois, in_ch, out_ch):
        super().__init__()
        self.weight = nn.Parameter(torch.empty(out_ch, in_ch, n_rois))
        self.bias = nn.Parameter(torch.zeros(out_ch))
        nn.init.xavier_uniform_(self.weight)

    def forward(self, x):
        z = torch.einsum('bcn,fcn->bf', x.squeeze(-1), self.weight)
        return (z + self.bias[None, :])[:, :, None, None]


class BrainNetCNN(nn.Module):
    """BrainNetCNN compacta E2E(8) -> E2N(16) -> N2G(16), para 190 ROIs."""
    def __init__(self, n_rois=190, e2e=8, e2n=16, n2g=16, dropout=0.5):
        super().__init__()
        self.e2e = nn.Sequential(E2E(n_rois, 1, e2e), nn.LeakyReLU(0.33))
        self.e2n = nn.Sequential(E2N(n_rois, e2e, e2n), nn.LeakyReLU(0.33), nn.Dropout(dropout))
        self.n2g = nn.Sequential(N2G(n_rois, e2n, n2g), nn.LeakyReLU(0.33))
        self.classifier = nn.Linear(n2g, 1)

    def forward(self, x):
        x = self.e2e(x)
        x = self.e2n(x)
        x = self.n2g(x)
        return self.classifier(x.flatten(1)).squeeze(1)
