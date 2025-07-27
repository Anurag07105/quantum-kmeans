from typing import Tuple
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from pathlib import Path
from config import DATASET_PATH

def load_and_preprocess_data(data_path: str = str(DATASET_PATH)) -> Tuple[np.ndarray, StandardScaler, list]:
    """Load and preprocess the Wholesale customers dataset."""
    # Load the wholesale customers dataset
    data = pd.read_csv(data_path)
    
    # Extract feature names
    feature_names = data.columns.tolist()
    
    # Convert to numpy array
    data_array = data.values
    
    # Scale the features
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data_array)
    
    # Apply PCA to reduce dimensionality while preserving most important features
    pca = PCA(n_components=2)
    scaled_data = pca.fit_transform(scaled_data)
    
    print(f"Loaded dataset shape: {scaled_data.shape}")
    print(f"Explained variance ratio: {pca.explained_variance_ratio_}")
    
    return scaled_data, scaler, feature_names

def split_dataset(data: np.ndarray, train_size: float = 0.8) -> Tuple[np.ndarray, np.ndarray]:
    """Split dataset into training and testing sets."""
    n_samples = data.shape[0]
    n_train = int(n_samples * train_size)
    
    # Shuffle indices
    indices = np.random.permutation(n_samples)
    train_indices = indices[:n_train]
    test_indices = indices[n_train:]
    
    return data[train_indices], data[test_indices]