
# Transformer from Scratch

```
Titel : Transformer from Scratch
Author: Tino Zalac
```

> ⚠️ Work in Progress – actively being developed.




> claude Readme  - ⚠️ überarbeiten 

A minimal, readable implementation of the Transformer architecture in pure PyTorch — no high-level abstractions, no magic.

Built to understand how attention and transformers actually work, not just how to call them.

## What this implements

- Scaled Dot-Product Attention
- Multi-Head Attention
- Positional Encoding
- Feed-Forward layers & Layer Normalization
- A complete GPT-style Transformer
- Training on a small text dataset

## The core formula

```
Attention(Q, K, V) = softmax(QK^T / √d) · V
```

## Structure

```
transformer-from-scratch/
├── attention.py             # Scaled dot-product & multi-head attention
├── positional_encoding.py   # Sinusoidal positional encoding
├── transformer.py           # Feed-forward, layer norm, transformer block
├── model.py                 # Full GPT-style model
├── train.py                 # Training loop
└── requirements.txt
```

## Requirements



## Background


