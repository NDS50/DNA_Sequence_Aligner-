from algorithm.needleman_wunsch import run_needleman_wunsch
from visualization.matrix_heatmap import plot_alignment_heatmap  # <--- IMPORT THIS
import numpy as np

def main():
    # 1. Define your test data
    sequence_A = "GATTACA"
    sequence_B = "GCATGCU" 
    
    # 2. Run the algorithm
    aligned_a, aligned_b, final_score, matrix = run_needleman_wunsch(
        sequence_A, 
        sequence_B
    )
    
    # 3. Output text results
    print(f"--- DNA Alignment Results ---")
    print(f"Sequence 1: {aligned_a}")
    print(f"Sequence 2: {aligned_b}")
    print(f"Final Score: {final_score}")
    
    # 4. Visualize!
    print("\nGenerating Heatmap...")
    plot_alignment_heatmap(matrix, sequence_A, sequence_B)

if __name__ == "__main__":
    main()
