import time
import numpy as np
from typing import Tuple
from sklearn.cluster import KMeans

def measure_clustering_performance(data: np.ndarray, n_clusters: int = 3) -> Tuple[np.ndarray, np.ndarray, float, float]:
    """Measure clustering performance without direct quantum imports."""
    # Classical K-means
    classical_start = time.time()
    classical_kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    classical_labels = classical_kmeans.fit_predict(data)
    classical_time = time.time() - classical_start
    
    # Import quantum implementation here to avoid circular imports
    from src.quantum.quantum_kmeans import QuantumKMeans
    
    # Quantum K-means
    quantum_start = time.time()
    quantum_kmeans = QuantumKMeans(n_clusters=n_clusters)
    quantum_labels = quantum_kmeans.fit(data)
    quantum_time = time.time() - quantum_start
    
    return classical_labels, quantum_labels, classical_time, quantum_time
