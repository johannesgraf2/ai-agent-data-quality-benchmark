"""
Simple Example: End-to-End Benchmark Flow
Shows exactly how the benchmark works with ONE task
"""

import pandas as pd
import sys
sys.path.append('..')
from metrics.f1_score import compute_confusion_matrix, compute_detection_metrics
from metrics.corruption import compute_corruption_rate
from metrics.drift import compute_global_drift


# ============= STEP 1: Original Clean Dataset =============
print("=" * 60)
print("STEP 1: Original Clean Dataset")
print("=" * 60)

clean_data = pd.DataFrame({
    "order_id": [1001, 1002, 1003],
    "product": ["Laptop", "Mouse", "Keyboard"],
    "price": [999.99, 29.99, 79.99],
    "date": ["2024-01-15", "2024-01-16", "2024-01-17"]
})

print(clean_data)
print()


# ============= STEP 2: Inject Errors =============
print("=" * 60)
print("STEP 2: Inject Errors (Accuracy Issues)")
print("=" * 60)

dirty_data = clean_data.copy()
# Row 0: Wrong price (inject accuracy error)
dirty_data.loc[0, "price"] = 9999.99
# Row 2: Invalid date (inject accuracy error)
dirty_data.loc[2, "date"] = "2024-13-99"

# Track which rows have errors
error_mask = [True, False, True]  # Rows 0 and 2 have errors

print(dirty_data)
print(f"\nInjected errors in rows: {[i for i, e in enumerate(error_mask) if e]}")
print()


# ============= STEP 3: AI Agent Cleans It =============
print("=" * 60)
print("STEP 3: AI Agent Cleans the Data")
print("=" * 60)

# In real benchmark, this would call Gemini/GPT/Claude API
# For this example, we simulate perfect agent output
agent_output = pd.DataFrame({
    "order_id": [1001, 1002, 1003],
    "product": ["Laptop", "Mouse", "Keyboard"],
    "price": [999.99, 29.99, 79.99],        # Fixed row 0
    "date": ["2024-01-15", "2024-01-16", "2024-01-17"]  # Fixed row 2
})

print(agent_output)
print("\n✅ Agent fixed both errors!")
print()


# ============= STEP 4: Compute Metrics =============
print("=" * 60)
print("STEP 4: Compute Metrics")
print("=" * 60)

# For each row, did the agent fix it correctly?
# We need to compare cell-by-cell to determine TP/FP/TN/FN

tp = 0  # True Positive: fixed an error
fp = 0  # False Positive: damaged clean data
tn = 0  # True Negative: left clean data alone
fn = 0  # False Negative: missed an error

for i in range(len(clean_data)):
    row_had_error = error_mask[i]
    
    # Compare agent output to clean data (ground truth)
    agent_row = agent_output.iloc[i]
    clean_row = clean_data.iloc[i]
    
    # Did agent change anything?
    row_was_changed = not agent_row.equals(clean_row)
    
    # Is agent's output correct (matches ground truth)?
    agent_correct = agent_row.equals(clean_row)
    
    if row_had_error:
        if agent_correct:
            tp += 1  # Fixed the error correctly
            print(f"Row {i}: ✅ TP - Fixed error correctly")
        else:
            fn += 1  # Missed the error or fixed incorrectly
            print(f"Row {i}: ❌ FN - Missed error or fixed wrong")
    else:
        if agent_correct:
            tn += 1  # Correctly left clean data alone
            print(f"Row {i}: ✅ TN - Left clean data alone")
        else:
            fp += 1  # Damaged clean data
            print(f"Row {i}: ❌ FP - Damaged clean data")

print()

# Compute detection metrics
metrics = compute_detection_metrics(tp, fp, tn, fn)
print("=" * 60)
print("DETECTION METRICS")
print("=" * 60)
print(f"F1 Score:        {metrics['f1']:.3f}")
print(f"Precision:       {metrics['precision']:.3f}")
print(f"Recall:          {metrics['recall']:.3f}")
print(f"Specificity:     {metrics['specificity']:.3f}")
print()
print(f"TP: {tp}  FP: {fp}  TN: {tn}  FN: {fn}")
print()


# ============= STEP 5: Corruption Rate =============
print("=" * 60)
print("STEP 5: Corruption Rate (Safety Check)")
print("=" * 60)

# Protected column: order_id should NEVER be modified
protected_columns = ["order_id", "product"]

corruption = compute_corruption_rate(
    original_df=clean_data,
    agent_output_df=agent_output,
    protected_columns=protected_columns,
    injected_row_indices=[0, 2]  # Only rows with errors
)

print(f"Corruption Rate: {corruption['corruption_rate']:.3f}")
print(f"Edits in protected columns: {corruption['edits_in_protected']}")
print(f"Protected columns affected: {corruption['protected_columns_affected']}")
print()


# ============= STEP 6: Distribution Drift =============
print("=" * 60)
print("STEP 6: Distribution Drift (Statistical Check)")
print("=" * 60)

drift = compute_global_drift(
    original_df=clean_data,
    cleaned_df=agent_output
)

print(f"Global Drift Score: {drift['global_drift']:.3f}")
print("Per-column drift:")
for col, score in drift['by_column'].items():
    print(f"  {col}: {score:.3f}")
print()


# ============= SUMMARY =============
print("=" * 60)
print("FINAL SUMMARY")
print("=" * 60)
print(f"✅ F1 Score:        {metrics['f1']:.3f}")
print(f"✅ Corruption Rate: {corruption['corruption_rate']:.3f}")
print(f"✅ Drift Score:     {drift['global_drift']:.3f}")
print()
print("This is ONE task. Your thesis will run 108 tasks like this!")
print("=" * 60)
