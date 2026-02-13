# 📊 Data Integration Guide

This dashboard is built to display your benchmark results. Here's how to plug in your real data when you have it.

## Dashboard Structure

The dashboard shows **3 aggregate scores per model**:
1. **Performance Score** - Aggregate of F1, precision, recall
2. **Safety Score** - Aggregate of corruption rate, drift  
3. **Operational Score** - Aggregate of reliability, robustness, auditability

Plus **4 dimension scores**:
- Accuracy
- Completeness
- Consistency
- Uniqueness

## Option 1: Update Mock Data (Quick & Easy)

### Frontend (React)
Edit `/frontend/src/App.jsx` lines 8-48:

```javascript
const MOCK_DATA = {
  models: [
    {
      id: 'your-model-id',
      name: 'Your Model Name',
      scores: {
        performance: 0.XX,  // Your calculated performance score
        safety: 0.XX,       // Your calculated safety score
        operational: 0.XX   // Your calculated operational score
      }
    },
    // Add more models...
  ],
  dimensionBreakdown: {
    'your-model-id': {
      accuracy: 0.XX,
      completeness: 0.XX,
      consistency: 0.XX,
      uniqueness: 0.XX
    },
    // Add more models...
  }
}
```

### Backend (Python API)
Edit `/backend/api/main.py` lines 45-90:

```python
MOCK_MODELS = [
    {
        "id": "your-model-id",
        "name": "Your Model Name",
        "scores": {
            "performance": 0.XX,
            "safety": 0.XX,
            "operational": 0.XX
        }
    }
]

MOCK_DIMENSIONS = {
    "your-model-id": {
        "accuracy": 0.XX,
        "completeness": 0.XX,
        "consistency": 0.XX,
        "uniqueness": 0.XX
    }
}
```

## Option 2: API Integration (Production-Ready)

### 1. Calculate Your Aggregate Scores

**Performance Score Formula:**
```python
performance_score = (f1_score + precision + recall) / 3
```

**Safety Score Formula:**
```python
# Invert corruption rate (higher is better)
safety_score = ((1 - corruption_rate) + (1 - drift_score)) / 2
```

**Operational Score Formula:**
```python
operational_score = (reliability + robustness + auditability) / 3
```

### 2. POST Data to API

```python
import requests

# Update model scores
models_data = [
    {
        "id": "gemini-3-pro",
        "name": "Google Gemini 3 Pro",
        "scores": {
            "performance": 0.87,
            "safety": 0.92,
            "operational": 0.85
        }
    }
]

response = requests.post(
    "http://localhost:8000/api/models/update",
    json=models_data
)

# Update dimensions
dimensions_data = {
    "accuracy": 0.89,
    "completeness": 0.85,
    "consistency": 0.88,
    "uniqueness": 0.86
}

response = requests.post(
    "http://localhost:8000/api/dimensions/update",
    params={"model_id": "gemini-3-pro"},
    json=dimensions_data
)
```

### 3. Connect Frontend to Backend

The frontend is already configured to fetch from `/api/models` and `/api/dimensions/{model_id}`.

If you want to use live API data instead of mock data:

Edit `/frontend/src/App.jsx`:

```javascript
import { useState, useEffect } from 'react'
import axios from 'axios'

function App() {
  const [modelsData, setModelsData] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    // Fetch from API
    axios.get('http://localhost:8000/api/models')
      .then(response => setModelsData(response.data))
      .catch(error => console.error(error))
      .finally(() => setLoading(false))
  }, [])

  if (loading) return <div>Loading...</div>

  // Use modelsData instead of MOCK_DATA
  // ...
}
```

## Option 3: JSON File (Simplest)

Create `/frontend/public/data.json`:

```json
{
  "models": [
    {
      "id": "gemini-3-pro",
      "name": "Google Gemini 3 Pro",
      "scores": {
        "performance": 0.87,
        "safety": 0.92,
        "operational": 0.85
      }
    }
  ],
  "dimensions": {
    "gemini-3-pro": {
      "accuracy": 0.89,
      "completeness": 0.85,
      "consistency": 0.88,
      "uniqueness": 0.86
    }
  }
}
```

Load it in your app:

```javascript
fetch('/data.json')
  .then(res => res.json())
  .then(data => setModelsData(data))
```

## Calculating Aggregate Scores

### From Raw Metrics to Dashboard Scores

When you have your benchmark results (F1, precision, recall, corruption rate, etc.), calculate the 3 aggregate scores:

```python
def calculate_performance_score(f1, precision, recall):
    """Average of detection metrics"""
    return (f1 + precision + recall) / 3

def calculate_safety_score(corruption_rate, drift_score):
    """Inverse of safety risks (higher = safer)"""
    # Corruption and drift are BAD, so we invert them
    return ((1 - corruption_rate) + (1 - drift_score)) / 2

def calculate_operational_score(reliability, robustness, auditability):
    """Average of operational readiness metrics"""
    return (reliability + robustness + auditability) / 3
```

## Example: Full Integration Script

```python
# calculate_scores.py - Run after your benchmark
import json

# Your raw benchmark results
raw_results = {
    "gemini-3-pro": {
        "f1": 0.89,
        "precision": 0.87,
        "recall": 0.85,
        "corruption_rate": 0.08,
        "drift_score": 0.10,
        "reliability": 0.92,
        "robustness": 0.83,
        "auditability": 0.80,
        "dimensions": {
            "accuracy": 0.89,
            "completeness": 0.85,
            "consistency": 0.88,
            "uniqueness": 0.86
        }
    }
}

# Calculate aggregates
def process_model(model_id, results):
    performance = (results["f1"] + results["precision"] + results["recall"]) / 3
    safety = ((1 - results["corruption_rate"]) + (1 - results["drift_score"])) / 2
    operational = (results["reliability"] + results["robustness"] + results["auditability"]) / 3
    
    return {
        "id": model_id,
        "name": model_id.replace("-", " ").title(),
        "scores": {
            "performance": round(performance, 3),
            "safety": round(safety, 3),
            "operational": round(operational, 3)
        },
        "dimensions": results["dimensions"]
    }

# Process all models
dashboard_data = {
    "models": [process_model(mid, res) for mid, res in raw_results.items()]
}

# Save to JSON
with open("frontend/public/data.json", "w") as f:
    json.dump(dashboard_data, f, indent=2)

print("✅ Dashboard data generated!")
```

## Next Steps

1. **Now**: Use mock data to develop/test the dashboard
2. **Later**: Run your benchmarks and collect raw metrics
3. **Then**: Use one of the options above to plug in real data
4. **Finally**: Deploy the dashboard with your results

The dashboard is **ready to use** — just swap the data when you have it! 🦞
