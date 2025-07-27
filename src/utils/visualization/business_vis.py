import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, Any

def plot_inventory_analysis(ax, clusters, inventory_data: Dict, title: str):
    """Plot inventory management analysis."""
    width = 0.35
    ax.bar(clusters, inventory_data['cluster_demands'], width, label='Demand')
    ax.bar([x + width for x in clusters], inventory_data['stock_levels'], 
           width, label='Stock')
    ax.set_title(title)
    ax.set_xlabel('Customer Segment')
    ax.set_ylabel('Units')
    ax.legend()

def plot_pricing_analysis(ax, clusters, pricing_data: Dict, title: str):
    """Plot pricing strategy analysis."""
    scatter = ax.scatter(pricing_data['price_sensitivity'],
                        pricing_data['customer_value'],
                        c=range(len(clusters)), 
                        cmap='viridis', 
                        s=100)
    ax.set_title(title)
    ax.set_xlabel('Price Sensitivity')
    ax.set_ylabel('Customer Value ($)')
    return scatter

def get_business_recommendations(method: str = 'classical') -> list:
    """Get business recommendations based on analysis method."""
    if method == 'classical':
        return [
            "Segment A: High-value customers - Premium pricing strategy",
            "Segment B: Price-sensitive - Targeted promotions",
            "Segment C: Moderate spenders - Loyalty programs",
            "Segment D: Occasional buyers - Engagement campaigns"
        ]
    else:  # quantum
        return [
            "Segment A: Premium - Dynamic pricing + VIP services",
            "Segment B: Value - Optimized discount scheduling",
            "Segment C: Regular - Balanced inventory management",
            "Segment D: Variable - Personalized marketing"
        ]

def plot_business_dashboard(data: np.ndarray,
                          labels: np.ndarray,
                          centroids: np.ndarray,
                          inventory_data: Dict,
                          pricing_data: Dict,
                          title: str,
                          method: str = 'classical',
                          save_path: str = None):
    """Create comprehensive business analytics dashboard."""
    plt.figure(figsize=(15, 10))
    
    # Inventory Analysis
    ax1 = plt.subplot(221)
    plot_inventory_analysis(
        ax1, 
        range(len(centroids)), 
        inventory_data,
        f"{method.capitalize()} Inventory Analysis"
    )
    
    # Pricing Analysis
    ax2 = plt.subplot(222)
    scatter = plot_pricing_analysis(
        ax2, 
        centroids, 
        pricing_data,
        f"{method.capitalize()} Pricing Strategy"
    )
    plt.colorbar(scatter, ax=ax2, label='Segment')
    
    # Recommendations
    ax3 = plt.subplot(212)
    recommendations = get_business_recommendations(method)
    ax3.text(0.1, 0.5, '\n'.join(recommendations), fontsize=10)
    ax3.axis('off')
    
    plt.suptitle(title)
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path)
    plt.show()
