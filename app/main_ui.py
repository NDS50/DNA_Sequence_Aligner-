import streamlit as st
import sys
import os

# Add the parent directory to sys.path so we can import 'algorithm' and 'visualization'
# This is necessary because this file is inside the 'app/' folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from algorithm.needleman_wunsch import run_needleman_wunsch
from visualization.matrix_heatmap import plot_alignment_heatmap

# --- Page Config ---
st.set_page_config(page_title="DNA Aligner", page_icon="🧬", layout="wide")

# --- Header ---
st.title("🧬 DNA Sequence Aligner")
st.markdown("Use the **Needleman-Wunsch algorithm** to align two DNA sequences globally.")

# --- Sidebar: Inputs ---
st.sidebar.header("Alignment Settings")

# Default sequences
default_seq1 = "GATTACA"
default_seq2 = "GCATGCU"

seq1 = st.sidebar.text_input("Sequence 1 (Top)", value=default_seq1).upper()
seq2 = st.sidebar.text_input("Sequence 2 (Left)", value=default_seq2).upper()

st.sidebar.subheader("Scoring Parameters")
match_score = st.sidebar.number_input("Match Score (+)", value=1)
mismatch_score = st.sidebar.number_input("Mismatch Score (-)", value=-1)
gap_penalty = st.sidebar.number_input("Gap Penalty (-)", value=-2)

# --- Main Logic ---
if st.button("Run Alignment"):
    if not seq1 or not seq2:
        st.error("Please enter both sequences.")
    else:
        # 1. Run Algorithm
        align1, align2, score, matrix = run_needleman_wunsch(
            seq1, seq2, match_score, mismatch_score, gap_penalty
        )
        
        # 2. Display Results (Text)
        st.subheader("Results")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Final Alignment Score", score)
        
        # Display aligned sequences in code block for monospaced font
        st.text("Alignment:")
        st.code(f"{align1}\n{align2}", language="text")

        # 3. Display Results (Visual)
        st.subheader("Scoring Matrix Heatmap")
        fig = plot_alignment_heatmap(matrix, seq1, seq2)
        st.pyplot(fig)

else:
    st.info("Adjust settings in the sidebar and click 'Run Alignment' to start.")
