import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, Any
import time

def plot_quantum_results(data: np.ndarray, 
                        labels: np.ndarray, 
                        centroids: np.ndarray, 
                        execution_time: float,
                        circuit_stats: Dict[str, float],
                        save_path: str = None):
    """Plot quantum K-means results with quantum-specific metrics."""
    plt.figure(figsize=(15, 8))
    
    # Plot clusters
    plt.subplot(121)
    scatter = plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis')
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x', s=200, linewidth=3)
    plt.title(f'Quantum K-means Clustering\nExecution Time: {execution_time:.4f} seconds')
    plt.colorbar(scatter)
    
    # Plot quantum metrics
    plt.subplot(122)
    metrics = ['Circuit Execution', 'State Preparation', 'Measurement', 'Total Time']
    values = [
        circuit_stats.get('circuit_time', 0),
        circuit_stats.get('prep_time', 0),
        circuit_stats.get('measure_time', 0),
        execution_time
    ]
    plt.bar(metrics, values)
    plt.xticks(rotation=45)
    plt.ylabel('Time (seconds)')
    plt.title('Quantum K-means Performance Breakdown')
    
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path)
    plt.show()
