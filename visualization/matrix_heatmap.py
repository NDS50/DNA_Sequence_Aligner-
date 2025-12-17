import seaborn as sns
import matplotlib.pyplot as plt

def plot_alignment_heatmap(score_matrix, seq1, seq2):
    """
    Generates a heatmap figure.
    """
    x_labels = ["-"] + list(seq1)
    y_labels = ["-"] + list(seq2)
    
    # Create the figure explicitly
    fig, ax = plt.subplots(figsize=(10, 8))
    
    sns.heatmap(
        score_matrix, 
        xticklabels=x_labels, 
        yticklabels=y_labels, 
        annot=True, 
        cmap="viridis", 
        fmt='g',
        linewidths=.5,
        ax=ax
    )
    
    plt.title("Needleman-Wunsch Scoring Matrix")
    plt.xlabel("Sequence 1")
    plt.ylabel("Sequence 2")
    
    # CHANGE: Return the figure object instead of showing it
    return fig
