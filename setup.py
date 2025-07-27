from setuptools import setup, find_packages

setup(
    name="quantum-kmeans",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'numpy>=1.21.0',
        'pandas>=1.3.0',
        'qiskit>=0.39.0',
        'qiskit[visualization]>=0.39.0',
        'scikit-learn>=0.24.2',
        'matplotlib>=3.4.3',
        'seaborn>=0.11.2',
        'pytest>=7.0.0',
    ],
    python_requires='>=3.9',
)