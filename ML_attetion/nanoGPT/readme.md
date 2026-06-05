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

```bash
pip install torch numpy matplotlib
```

## Background

Companion project to my Bachelor's thesis on approximation algorithms and LP relaxations — exploring how optimization thinking applies to modern ML architectures.

Inspired by Andrej Karpathy's [nanoGPT](https://github.com/karpathy/nanoGPT).



# Todo – Gap Year Vorbereitung

## Sofort (Juni)

### Bewerbungsunterlagen
- [ ] GitHub Username in CV eintragen
- [ ] CV finalisieren (Kolloquium-Datum aktualisieren)
- [ ] Notebook Bachelorarbeit auf GitHub hochladen
- [ ] README für multistage-vertex-cover schreiben

### Bewerbungen
- [ ] Vector Informatik – Praktikum GenAI/LLMs (RDX-522)
  - [ ] Anschreiben finalisieren (Verfügbarkeit + Dauer ergänzen)
  - [ ] CV + Anschreiben einreichen

### Finanzen & Organisation
- [ ] ZSB Gespräch nächste Woche vorbereiten
  - [ ] Fragen zu elternunabhängigem BAföG
  - [ ] Krankenversicherung nach Studienende klären
  - [ ] Überbrückungsfinanzierung Oktober

---

## Juli – August

### Bachelorarbeit
- [ ] Abgabe Anfang September
- [ ] Kolloquium Mitte September vorbereiten

### Aktiv bewerben
- [ ] LinkedIn täglich checken
- [ ] 3–5 Bewerbungen pro Woche
- [ ] Fokus: Data Analyst, Operations Research, Optimierung – Berlin
- [ ] Firmen: Delivery Hero, Zalando, Flixbus, HERE Technologies

### Transformer Projekt
- [ ] PyTorch Basics lernen (1 Tag)
- [ ] Karpathy Video anschauen
- [ ] `attention.py` implementieren
- [ ] `positional_encoding.py` implementieren
- [ ] `transformer.py` implementieren
- [ ] `model.py` zusammenbauen
- [ ] `train.py` – auf Shakespeare-Datensatz trainieren
- [ ] Auf GitHub hochladen

---

## September

- [ ] Bachelorarbeit abgeben
- [ ] Kolloquium
- [ ] KIT Bescheid abwarten
- [ ] Falls nötig: weitere Bewerbungen

---

## Master (2027 – kein Stress jetzt)

- [ ] Telc B2 / IELTS machen
- [ ] Uni-Bescheinigung englischsprachige Lehrveranstaltungen anfordern
- [ ] Bewerbung FU Berlin M.Sc. Data Science (Deadline ~Mai 2027)
- [ ] Bewerbung LMU München (Deadline ~Juli 2027)
- [ ] Bewerbung RWTH Aachen (Deadline ~Juli 2027)