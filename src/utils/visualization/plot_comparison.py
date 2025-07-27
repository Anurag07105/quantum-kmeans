import matplotlib.pyplot as plt
from typing import Dict, Any

def plot_comparison(classical_results: Dict[str, Any], 
                   quantum_results: Dict[str, Any], 
                   output_path: str) -> None:
    """Plot classical vs quantum clustering results."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot classical results
    scatter1 = ax1.scatter(classical_results['data'][:, 0], 
                          classical_results['data'][:, 1], 
                          c=classical_results['labels'])
    ax1.scatter(classical_results['centroids'][:, 0], 
                classical_results['centroids'][:, 1], 
                c='red', marker='x', s=200, label='Centroids')
    ax1.set_title('Classical K-means')
    
    # Plot quantum results
    scatter2 = ax2.scatter(quantum_results['data'][:, 0], 
                          quantum_results['data'][:, 1], 
                          c=quantum_results['labels'])
    ax2.scatter(quantum_results['centroids'][:, 0], 
                quantum_results['centroids'][:, 1], 
                c='red', marker='x', s=200, label='Centroids')
    ax2.set_title('Quantum K-means')
    
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
