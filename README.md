# 🧬 DNA Sequence Aligner & Visualizer

### A Bioinformatics Tool for Global Pairwise Sequence Alignment

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-ff4b4b)
![NumPy](https://img.shields.io/badge/Library-NumPy-013243)
![Status](https://img.shields.io/badge/Status-Active-success)

## 📖 Overview
This project is an interactive bioinformatics tool designed to perform **Global Pairwise DNA Alignment**. It implements the **Needleman-Wunsch algorithm** (Dynamic Programming) to align two DNA sequences by maximizing matches and minimizing mismatches/gaps.

The tool features a **Streamlit Web Interface** for easy user interaction and generates **Seaborn Heatmaps** to visualize the scoring matrix and the optimal alignment path.

This project was built as a learning-focused implementation to deeply understand dynamic programming–based sequence alignment used in bioinformatics.

## 🧪 Learning Focus

This project was developed to understand:
- Dynamic Programming using 2D matrices
- Traceback-based solution reconstruction
- Practical bioinformatics workflows


## 🚀 Key Features
* **Global Alignment Logic:** Custom implementation of the Needleman-Wunsch algorithm using NumPy for efficient matrix calculation.
* **Interactive UI:** Built with Streamlit, allowing users to input sequences manually or upload FASTA files.
* **Dynamic Visualization:** Generates a heatmap of the scoring matrix, helping users understand the decision path (Traceback) taken by the algorithm.
* **Customizable Scoring:** Users can adjust specific parameters:
    * Match Score (Reward)
    * Mismatch Penalty (Cost)
    * Gap Penalty (Cost)

## 🛠️ Tech Stack
* **Language:** Python
* **Computation:** NumPy (Matrix operations)
* **Visualization:** Matplotlib & Seaborn (Heatmaps)
* **Interface:** Streamlit (Web App)

## 📸 Screenshots

<img width="1470" height="799" alt="Screenshot 2025-12-17 at 3 51 23 PM" src="https://github.com/user-attachments/assets/b426a011-4bc3-42f4-9930-d9269078c5e1" />
<img width="1470" height="799" alt="Screenshot 2025-12-17 at 3 51 47 PM" src="https://github.com/user-attachments/assets/aea7beb5-b2e2-45bc-90d8-8806187fe647" />

## ⚙️ Installation & Usage

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/DNA-Sequence-Aligner.git](https://github.com/YOUR_USERNAME/DNA-Sequence-Aligner.git)
cd DNA-Sequence-Aligner


