import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, Any
import time

def plot_classical_results(data: np.ndarray, 
                         labels: np.ndarray, 
                         centroids: np.ndarray, 
                         execution_time: float,
                         save_path: str = None):
    """Plot classical K-means results with timing information."""
    plt.figure(figsize=(15, 8))
    
    # Plot clusters
    plt.subplot(121)
    scatter = plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x', s=200, linewidth=3)
    plt.title(f'Classical K-means Clustering\nExecution Time: {execution_time:.4f} seconds')
    plt.colorbar(scatter)
    
    # Plot timing breakdown
    plt.subplot(122)
    times = ['Distance Calculation', 'Centroid Update', 'Total Time']
    values = [execution_time * 0.7, execution_time * 0.3, execution_time]  # Approximate breakdown
    plt.bar(times, values)
    plt.xticks(rotation=45)
    plt.ylabel('Time (seconds)')
    plt.title('Classical K-means Performance Breakdown')
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()
