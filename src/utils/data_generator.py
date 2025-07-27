import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def generate_expanded_dataset(n_samples=100000):
    """Generate synthetic wholesale customer data."""
    # Load original data for distribution reference
    original_data = pd.read_csv('data/Wholesale_customers.csv')
    
    # Calculate statistics of original data
    means = original_data.mean()
    stds = original_data.std()
    
    # Generate synthetic data following similar distributions
    synthetic_data = pd.DataFrame()
    for column in original_data.columns:
        if column in ['Channel', 'Region']:
            synthetic_data[column] = np.random.choice(original_data[column], size=n_samples)
        else:
            synthetic_data[column] = np.random.normal(
                loc=means[column],
                scale=stds[column],
                size=n_samples
            ).clip(0)  # Ensure no negative values
    
    # Save expanded dataset
    synthetic_data.to_csv('data/Wholesale_customers_expanded.csv', index=False)
    return synthetic_data

if __name__ == '__main__':
    generate_expanded_dataset()
