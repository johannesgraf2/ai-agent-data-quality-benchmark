"""
FastAPI Backend for AI Agent Data Quality Benchmark Dashboard
Simplified: Focus on 3 aggregate scores per model
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List

app = FastAPI(
    title="AI Agent Data Quality Benchmark API",
    description="REST API for AI agent benchmark dashboard",
    version="1.0.0"
)

# CORS middleware for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============= Data Models =============

class ModelScores(BaseModel):
    performance: float  # Aggregate of F1, precision, recall
    safety: float       # Aggregate of corruption, drift
    operational: float  # Aggregate of reliability, robustness, auditability


class Model(BaseModel):
    id: str
    name: str
    scores: ModelScores


class DimensionScores(BaseModel):
    accuracy: float
    completeness: float
    consistency: float
    uniqueness: float


# ============= Mock Data =============
# Replace this with real data when you have it

MOCK_MODELS = [
    {
        "id": "gemini-3-pro",
        "name": "Google Gemini 3 Pro",
        "scores": {
            "performance": 0.87,
            "safety": 0.92,
            "operational": 0.85
        }
    },
    {
        "id": "gpt-5.1",
        "name": "OpenAI GPT-5.1",
        "scores": {
            "performance": 0.89,
            "safety": 0.88,
            "operational": 0.83
        }
    },
    {
        "id": "claude-4",
        "name": "Anthropic Claude 4",
        "scores": {
            "performance": 0.85,
            "safety": 0.90,
            "operational": 0.87
        }
    }
]

MOCK_DIMENSIONS = {
    "gemini-3-pro": {
        "accuracy": 0.89,
        "completeness": 0.85,
        "consistency": 0.88,
        "uniqueness": 0.86
    },
    "gpt-5.1": {
        "accuracy": 0.91,
        "completeness": 0.87,
        "consistency": 0.90,
        "uniqueness": 0.88
    },
    "claude-4": {
        "accuracy": 0.87,
        "completeness": 0.83,
        "consistency": 0.86,
        "uniqueness": 0.84
    }
}


# ============= API Endpoints =============

@app.get("/")
def read_root():
    return {
        "message": "AI Agent Data Quality Benchmark API",
        "docs": "/docs",
        "version": "1.0.0",
        "endpoints": [
            "/api/models",
            "/api/dimensions/{model_id}"
        ]
    }


@app.get("/api/models", response_model=List[Model])
def get_models():
    """
    Get all models with their 3 aggregate scores
    
    Returns list of models with:
    - performance: Aggregate of F1, precision, recall
    - safety: Aggregate of corruption rate, drift
    - operational: Aggregate of reliability, robustness, auditability
    """
    return MOCK_MODELS


@app.get("/api/dimensions/{model_id}", response_model=DimensionScores)
def get_dimensions(model_id: str):
    """
    Get dimension breakdown for a specific model
    
    Returns scores for 4 dimensions:
    - accuracy
    - completeness
    - consistency
    - uniqueness
    """
    if model_id not in MOCK_DIMENSIONS:
        return {"error": "Model not found"}, 404
    
    return MOCK_DIMENSIONS[model_id]


# ============= Data Update Endpoint =============

@app.post("/api/models/update")
def update_model_data(models: List[Model]):
    """
    Update model data (for when you have real benchmark results)
    
    POST your data here in this format:
    [
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
    """
    # In production, save to database
    # For now, just acknowledge
    return {
        "message": "Data received",
        "models_count": len(models)
    }


@app.post("/api/dimensions/update")
def update_dimension_data(model_id: str, dimensions: DimensionScores):
    """
    Update dimension breakdown for a model
    
    POST your data here:
    {
        "accuracy": 0.89,
        "completeness": 0.85,
        "consistency": 0.88,
        "uniqueness": 0.86
    }
    """
    # In production, save to database
    return {
        "message": "Dimensions updated",
        "model_id": model_id
    }


# ============= Development Server =============

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
