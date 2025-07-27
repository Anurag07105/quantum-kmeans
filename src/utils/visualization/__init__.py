from .comparison import plot_comparison
from .performance import measure_clustering_performance

def plot_clustering_comparison(*args, **kwargs):
    """Wrapper for backward compatibility"""
    from .comparison import plot_comparison
    return plot_comparison(*args, **kwargs)

__all__ = [
    'plot_comparison',
    'plot_clustering_comparison',
    'measure_clustering_performance'
]
