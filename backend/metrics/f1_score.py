"""
F1 Score and Detection Metrics
Metrics Agent: Core performance metrics for data quality remediation
"""

import numpy as np
from typing import Tuple, Dict


def compute_detection_metrics(
    true_positives: int,
    false_positives: int,
    true_negatives: int,
    false_negatives: int
) -> Dict[str, float]:
    """
    Compute F1, Precision, Recall, Specificity, TPR, FPR
    
    Args:
        true_positives: Correctly fixed errors
        false_positives: Incorrectly modified clean data
        true_negatives: Correctly left clean data alone
        false_negatives: Missed errors (not fixed)
    
    Returns:
        Dictionary with all detection metrics
    """
    # Handle edge cases
    if true_positives + false_positives == 0:
        precision = 0.0
    else:
        precision = true_positives / (true_positives + false_positives)
    
    if true_positives + false_negatives == 0:
        recall = 0.0
    else:
        recall = true_positives / (true_positives + false_negatives)
    
    if precision + recall == 0:
        f1 = 0.0
    else:
        f1 = 2 * (precision * recall) / (precision + recall)
    
    if true_negatives + false_positives == 0:
        specificity = 0.0
    else:
        specificity = true_negatives / (true_negatives + false_positives)
    
    # TPR = Recall (True Positive Rate)
    tpr = recall
    
    # FPR = False Positive Rate
    if false_positives + true_negatives == 0:
        fpr = 0.0
    else:
        fpr = false_positives / (false_positives + true_negatives)
    
    return {
        "f1": f1,
        "precision": precision,
        "recall": recall,
        "specificity": specificity,
        "true_positive_rate": tpr,
        "false_positive_rate": fpr,
        "support": {
            "tp": true_positives,
            "fp": false_positives,
            "tn": true_negatives,
            "fn": false_negatives
        }
    }


def compute_confusion_matrix(
    ground_truth: np.ndarray,
    agent_output: np.ndarray,
    error_injected_mask: np.ndarray
) -> Tuple[int, int, int, int]:
    """
    Compute confusion matrix for data quality remediation
    
    Args:
        ground_truth: Original clean data
        agent_output: Agent's cleaned data
        error_injected_mask: Boolean mask indicating which rows had injected errors
    
    Returns:
        Tuple of (TP, FP, TN, FN)
    """
    # TP: Agent fixed an error correctly
    tp = 0
    # FP: Agent modified clean data incorrectly
    fp = 0
    # TN: Agent correctly left clean data alone
    tn = 0
    # FN: Agent missed an error
    fn = 0
    
    for i in range(len(ground_truth)):
        was_error_injected = error_injected_mask[i]
        agent_changed_it = not np.array_equal(agent_output[i], ground_truth[i])
        agent_fixed_it = np.array_equal(agent_output[i], ground_truth[i])
        
        if was_error_injected:
            if agent_fixed_it:
                tp += 1  # Successfully fixed
            else:
                fn += 1  # Missed the error
        else:
            if agent_changed_it:
                fp += 1  # Damaged clean data
            else:
                tn += 1  # Correctly left it alone
    
    return tp, fp, tn, fn


# Example usage and tests
if __name__ == "__main__":
    # Test case: Perfect agent
    metrics = compute_detection_metrics(tp=10, fp=0, tn=90, fn=0)
    print("Perfect agent:", metrics)
    assert metrics["f1"] == 1.0
    
    # Test case: Balanced agent
    metrics = compute_detection_metrics(tp=7, fp=3, tn=87, fn=3)
    print("Balanced agent:", metrics)
    
    # Test case: Aggressive agent (high recall, low precision)
    metrics = compute_detection_metrics(tp=10, fp=20, tn=70, fn=0)
    print("Aggressive agent:", metrics)
    
    print("\nAll tests passed ✓")
