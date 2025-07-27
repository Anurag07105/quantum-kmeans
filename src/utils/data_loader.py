import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from typing import Tuple, Generator

def load_expanded_data(min_samples: int = 95000) -> Tuple[np.ndarray, int]:
    """Load and preprocess the expanded dataset."""
    # Load expanded data with numeric type enforcement
    df = pd.read_csv('data/Wholesale_customers_expanded.csv', 
                     dtype=float,
                     header=0,  # Assume first row is header
                     low_memory=False)
    
    print(f"Found {len(df)} samples in dataset")
    
    if len(df) < min_samples:
        raise ValueError(f"Dataset contains only {len(df)} samples, but {min_samples} required")
    
    # Convert to float32 for memory efficiency with large datasets
    feature_data = df.values.astype(np.float32)
    
    # Scale the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(feature_data)
    
    return X_scaled, len(X_scaled)

def load_data_in_batches(batch_size: int = 1000) -> Generator[np.ndarray, None, None]:
    """Load data in batches for memory efficiency."""
    X_scaled, _ = load_expanded_data()
    for i in range(0, len(X_scaled), batch_size):
        yield X_scaled[i:i + batch_size]

def get_data_shape() -> Tuple[int, int]:
    """Get the shape of the expanded dataset."""
    X_scaled, n_samples = load_expanded_data()
    return n_samples, X_scaled.shape[1]
