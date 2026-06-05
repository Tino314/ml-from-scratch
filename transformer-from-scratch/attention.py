import torch
import torch.nn as nn
import torch.nn.functional as F


def scaled_dot_product_attention(Q: torch.Tensor, K: torch.Tensor, V: torch.Tensor, mask: torch.Tensor = None) -> torch.Tensor:
    d = Q.shape[-1]

    scores  = torch.matmul(Q, K.transpose(-2, -1)) / torch.sqrt(torch.tensor(d, dtype=torch.float32))

    if mask is not None:
        scores = scores.masked_fill(mask == 0, float('-inf'))

    weights = F.softmax(scores, dim=-1)
    return torch.matmul(weights, V)


if __name__ == "__main__":
    Q = torch.randn(4, 8)
    K = torch.randn(4, 8)
    V = torch.randn(4, 8)
    out = scaled_dot_product_attention(Q, K, V)
    print("Output shape:", out.shape)  # sollte torch.Size([4, 8]) sein
    print("Output:\n", out)


class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        assert d_model % num_heads == 0
        
        self.d_model = d_model
        self.num_heads = num_heads
        self.d_k = d_model // num_heads  # dimension pro Head
        
        # Projektionsmatrizen
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)
    
    def forward(self, Q, K, V, mask=None):
        # hier kommt dein Code
        pass