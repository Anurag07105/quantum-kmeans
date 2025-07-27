# Quantum K-means Clustering Project

This project implements both classical and quantum K-means clustering algorithms for business analytics.

## Overview

The project consists of two main components:

1. **Classical K-Means**: A traditional implementation of the K-Means clustering algorithm.
2. **Quantum K-Means**: An enhanced version that utilizes quantum computing principles to optimize clustering.

## Dataset

The dataset used for this project is the `Wholesale_customers_final.csv`, which contains customer spending data across various product categories. This data is essential for performing clustering and understanding customer segments.

## Setup Instructions

### 1. Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

### 2. Clone the Repository

```bash
git clone https://github.com/yourusername/quantum-kmeans.git
cd quantum-kmeans
```

### 3. Create Virtual Environment

```bash
# On Windows
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Verify Qiskit Installation

```bash
python -c "import qiskit; print(qiskit.__version__)"
```

## Project Structure

```
quantum-kmeans/
├── src/
│   ├── classical/
│   ├── quantum/
│   ├── utils/
│   └── main.py
├── data/
│   └── Wholesale_customers_final.csv
├── requirements.txt
└── README.md
```

## Running the Project

1. Activate virtual environment (if not already activated):

```bash
# On Windows
.\venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

2. Run the main script:

```bash
python src/main.py
```

3. View Results:

- Classical clustering results will be displayed first
- Press Enter when prompted to continue with quantum analysis
- Results are saved in the 'output' directory

## Troubleshooting

1. If you encounter BLAS/LAPACK errors:

```bash
pip install --upgrade numpy scipy
```

2. For Qiskit backend issues:

```bash
pip install --upgrade qiskit-aer
```

3. For visualization issues:

```bash
pip install --upgrade matplotlib seaborn
```

## Notes

- Ensure you have sufficient RAM (minimum 4GB recommended)
- For optimal performance, close other resource-intensive applications
- Quantum simulation might be slower on systems with limited processing power

## Additional Resources

- Qiskit Documentation: https://qiskit.org/documentation/
- Quantum K-means Paper: [Add relevant paper link]
- Classical K-means Documentation: https://scikit-learn.org/stable/modules/clustering.html

## Testing

Unit tests are provided for both the classical and quantum K-Means implementations. To run the tests, use the following command:

```bash
pytest tests/
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

[Add your license information]
