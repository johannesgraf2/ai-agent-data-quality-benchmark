# 🔥 AI Agent Data Quality Benchmark Dashboard

A comprehensive benchmarking system for evaluating autonomous AI agents on data quality remediation tasks.

## 🎯 Core Objective

Measure how well autonomous agents fix data quality issues across four dimensions:
- **Accuracy** - Correcting factually wrong data
- **Completeness** - Filling missing values
- **Consistency** - Resolving contradictions
- **Uniqueness** - Removing duplicates

**Primary Metric:** F1 Score (harmonic mean of precision and recall)

## 📊 Key Metrics

### Primary Performance
- **F1 Score** - Global and per-dimension
- **Precision** - Avoidance of clean data damage
- **Recall** - Detection and correction of injected errors
- **Specificity, TPR, FPR** - Supporting detection metrics

### Safety & Integrity
- **Corruption Rate** - Edits in protected columns / total injected rows
- **Distribution Drift** - Statistical deviation (KL divergence, Wasserstein distance)

### Operational Readiness (Thesis Unique Contribution)
- **Reliability** - Consistency across identical task executions
- **Robustness** - Performance under perturbations
- **Auditability** - LLM-as-judge explanation quality

## 🧠 Models Supported
- Google Gemini 3 Pro (primary focus)
- OpenAI GPT-5.1
- Anthropic Claude 4
- Extensible architecture for additional models

## 🏗️ Architecture

### Agent-Based Design
This project uses specialized AI agents for different responsibilities:
- **Metrics Agent** - Computes F1, precision, recall, corruption, drift
- **Visualization Agent** - Builds charts, dashboards, and UI components
- **Backend Agent** - API design, data pipelines, benchmark execution
- **Research Agent** - Academic accuracy, statistical methods, documentation

### Tech Stack
- **Frontend:** React + D3.js / Chart.js for visualizations
- **Backend:** Python (FastAPI) for metrics computation
- **Data Processing:** pandas, numpy, scipy for statistics
- **Benchmark Execution:** Orchestration for multi-model runs

## 📂 Project Structure
```
/
├── agents/              # Agent configurations
├── frontend/            # React dashboard
├── backend/             # Python API + metrics
├── benchmark/           # Task definitions + execution
├── data/                # Sample datasets
├── docs/                # Academic documentation
└── README.md
```

## 🚀 Getting Started
```bash
# Clone repository
git clone https://github.com/johannesgraf2/ai-agent-data-quality-benchmark.git
cd ai-agent-data-quality-benchmark

# Install dependencies
cd frontend && npm install
cd ../backend && pip install -r requirements.txt

# Run benchmark
python backend/run_benchmark.py

# Start dashboard
cd frontend && npm start
```

## 📈 Dashboard Views

### 1. Overview Page
- Global F1 (large KPI)
- Global corruption rate
- Global drift score
- F1 by dimension (4 bars)
- Reliability and robustness scores

### 2. Dimension Deep Dive
- Per-difficulty F1
- Confusion matrices
- Error-type breakdown
- Example corrections
- Drift analysis

### 3. Task-Level Explorer
- Original dataset preview
- Injected errors highlighted
- Agent output
- Diff visualization
- Metric breakdown
- Justification text (auditability)

## 🎓 Academic Context
This dashboard supports a master's thesis evaluating AI agents for data quality remediation, with focus on operational readiness metrics (reliability, robustness, auditability) beyond traditional ML performance metrics.

---

Built with 🦞 by specialized AI agents
