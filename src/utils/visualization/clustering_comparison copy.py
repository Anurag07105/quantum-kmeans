import numpy as np
import matplotlib.pyplot as plt

def plot_clustering_comparison(data: np.ndarray, 
                             classical_labels: np.ndarray, 
                             quantum_labels: np.ndarray,
                             classical_time: float,
                             quantum_time: float,
                             title: str = "Classical vs Quantum K-means Clustering") -> None:
    """Plot clustering results and performance comparison."""
    fig = plt.figure(figsize=(15, 5))
    
    # Plot classical clustering
    ax1 = fig.add_subplot(131)
    ax1.scatter(data[:, 0], data[:, 1], c=classical_labels, cmap='viridis')
    ax1.set_title(f'Classical K-means\nTime: {classical_time:.3f}s')
    
    # Plot quantum clustering
    ax2 = fig.add_subplot(132)
    ax2.scatter(data[:, 0], data[:, 1], c=quantum_labels, cmap='viridis')
    ax2.set_title(f'Quantum K-means\nTime: {quantum_time:.3f}s')
    
    # Plot time comparison
    ax3 = fig.add_subplot(133)
    times = [classical_time, quantum_time]
    bars = ax3.bar(['Classical', 'Quantum'], times)
    ax3.set_title('Execution Time Comparison')
    ax3.set_ylabel('Time (seconds)')
    
    # Add time values on top of bars
    for bar in bars:
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.3f}s',
                ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show()
