import numpy as np

def run_needleman_wunsch(seq1, seq2, match_score=1, mismatch_score=-1, gap_penalty=-2):
    """
    Executes the Needleman-Wunsch global alignment algorithm.
    
    Args:
        seq1 (str): First DNA sequence.
        seq2 (str): Second DNA sequence.
        match_score (int): Score for a match.
        mismatch_score (int): Penalty for a mismatch.
        gap_penalty (int): Penalty for a gap.
        
    Returns:
        tuple: (aligned_seq1, aligned_seq2, score, score_matrix)
    """
    
    # --- Step 1: Initialization ---
    n = len(seq1)
    m = len(seq2)
    
    # Create the grid (m+1 rows, n+1 cols)
    score_matrix = np.zeros((m + 1, n + 1))
    
    # Initialize first row and column with gap penalties
    for i in range(n + 1):
        score_matrix[0][i] = i * gap_penalty
    for j in range(m + 1):
        score_matrix[j][0] = j * gap_penalty
        
    # --- Step 2: Matrix Filling ---
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            
            # Calculate scores
            if seq1[j-1] == seq2[i-1]:
                diagonal = score_matrix[i-1][j-1] + match_score
            else:
                diagonal = score_matrix[i-1][j-1] + mismatch_score
            
            vertical = score_matrix[i-1][j] + gap_penalty
            horizontal = score_matrix[i][j-1] + gap_penalty
            
            # Fill cell with max score
            score_matrix[i][j] = max(diagonal, vertical, horizontal)
            
    # --- Step 3: Traceback ---
    align1 = ""
    align2 = ""
    i = m
    j = n
    
    while i > 0 and j > 0:
        current_score = score_matrix[i][j]
        diagonal_score = score_matrix[i-1][j-1]
        vertical_score = score_matrix[i-1][j]
        horizontal_score = score_matrix[i][j-1]
        
        # Determine match/mismatch score for the diagonal check
        if seq1[j-1] == seq2[i-1]:
            step_diag = match_score
        else:
            step_diag = mismatch_score
            
        if current_score == diagonal_score + step_diag:
            align1 += seq1[j-1]
            align2 += seq2[i-1]
            i -= 1
            j -= 1
        elif current_score == vertical_score + gap_penalty:
            align1 += "-"
            align2 += seq2[i-1]
            i -= 1
        elif current_score == horizontal_score + gap_penalty:
            align1 += seq1[j-1]
            align2 += "-"
            j -= 1
            
    # Handle remaining edge cases (top row or left col)
    while j > 0:
        align1 += seq1[j-1]
        align2 += "-"
        j -= 1
    while i > 0:
        align1 += "-"
        align2 += seq2[i-1]
        i -= 1
        
    return align1[::-1], align2[::-1], score_matrix[m][n], score_matrix

