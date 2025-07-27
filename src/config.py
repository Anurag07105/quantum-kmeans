from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent

# Data paths
DATA_DIR = PROJECT_ROOT / 'data'
DATASET_PATH = DATA_DIR / 'Wholesale_customers_final.csv'

# Output paths
OUTPUT_DIR = PROJECT_ROOT / 'output'
CLUSTERING_COMPARISON_PATH = OUTPUT_DIR / 'clustering_comparison.png'
