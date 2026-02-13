"""
Distribution Drift Metrics
Metrics Agent: Measure statistical deviation after cleaning
"""

import numpy as np
import pandas as pd
from scipy.stats import wasserstein_distance
from scipy.special import kl_div
from typing import Dict, Union


def compute_kl_divergence(original: pd.Series, cleaned: pd.Series) -> float:
    """
    Compute KL Divergence for categorical distributions
    Normalized to [0, 1] range
    
    Args:
        original: Original distribution (categorical)
        cleaned: Cleaned distribution (categorical)
    
    Returns:
        Normalized KL divergence score
    """
    # Get value counts as probabilities
    orig_counts = original.value_counts(normalize=True, dropna=False)
    clean_counts = cleaned.value_counts(normalize=True, dropna=False)
    
    # Align indices (handle new/missing categories)
    all_categories = set(orig_counts.index) | set(clean_counts.index)
    
    p = np.array([orig_counts.get(cat, 1e-10) for cat in all_categories])
    q = np.array([clean_counts.get(cat, 1e-10) for cat in all_categories])
    
    # Compute KL divergence
    kl = np.sum(kl_div(p, q))
    
    # Normalize to [0, 1] using sigmoid-like function
    # Small drift → 0, large drift → 1
    normalized = 1 - np.exp(-kl)
    
    return float(normalized)


def compute_wasserstein_distance_normalized(
    original: pd.Series,
    cleaned: pd.Series
) -> float:
    """
    Compute Wasserstein distance for numerical distributions
    Normalized to [0, 1] range
    
    Args:
        original: Original numerical values
        cleaned: Cleaned numerical values
    
    Returns:
        Normalized Wasserstein distance
    """
    # Remove NaN values
    orig_clean = original.dropna()
    clean_clean = cleaned.dropna()
    
    if len(orig_clean) == 0 or len(clean_clean) == 0:
        return 0.0
    
    # Compute Wasserstein distance
    distance = wasserstein_distance(orig_clean, clean_clean)
    
    # Normalize by the range of original data
    data_range = orig_clean.max() - orig_clean.min()
    if data_range == 0:
        return 0.0
    
    normalized = min(distance / data_range, 1.0)
    
    return float(normalized)


def compute_distribution_drift(
    original_df: pd.DataFrame,
    cleaned_df: pd.DataFrame,
    column: str
) -> Dict[str, Union[float, str]]:
    """
    Compute distribution drift for a single column
    Automatically detects categorical vs numerical
    
    Args:
        original_df: Original dataset
        cleaned_df: Cleaned dataset
        column: Column name to analyze
    
    Returns:
        Dictionary with drift score and method used
    """
    orig_col = original_df[column]
    clean_col = cleaned_df[column]
    
    # Detect column type
    if pd.api.types.is_numeric_dtype(orig_col):
        # Numerical: use Wasserstein distance
        drift_score = compute_wasserstein_distance_normalized(orig_col, clean_col)
        method = "wasserstein"
    else:
        # Categorical: use KL divergence
        drift_score = compute_kl_divergence(orig_col, clean_col)
        method = "kl_divergence"
    
    return {
        "column": column,
        "drift_score": drift_score,
        "method": method
    }


def compute_global_drift(
    original_df: pd.DataFrame,
    cleaned_df: pd.DataFrame,
    columns: list = None
) -> Dict[str, float]:
    """
    Compute global drift score across all (or specified) columns
    
    Args:
        original_df: Original dataset
        cleaned_df: Cleaned dataset
        columns: List of columns to analyze (None = all columns)
    
    Returns:
        Dictionary with per-column and global drift scores
    """
    if columns is None:
        columns = original_df.columns.tolist()
    
    drift_by_column = {}
    
    for col in columns:
        result = compute_distribution_drift(original_df, cleaned_df, col)
        drift_by_column[col] = result["drift_score"]
    
    # Global drift: average across all columns
    global_drift = np.mean(list(drift_by_column.values()))
    
    return {
        "global_drift": float(global_drift),
        "by_column": drift_by_column
    }


# Example usage
if __name__ == "__main__":
    # Test case: No drift
    df_original = pd.DataFrame({
        "category": ["A", "B", "A", "C"],
        "value": [10, 20, 15, 25]
    })
    
    df_cleaned = df_original.copy()
    
    result = compute_global_drift(df_original, df_cleaned)
    print("No drift:", result)
    assert result["global_drift"] < 0.01
    
    # Test case: Some drift
    df_cleaned_drift = df_original.copy()
    df_cleaned_drift.loc[0, "category"] = "C"  # Changed category
    df_cleaned_drift.loc[1, "value"] = 100      # Changed value significantly
    
    result = compute_global_drift(df_original, df_cleaned_drift)
    print("With drift:", result)
    assert result["global_drift"] > 0.1
    
    print("\nAll tests passed ✓")
