# 🚀 Quick Start Guide

## Prerequisites
- Python 3.10+
- Node.js 18+
- API keys for AI models (Gemini, GPT, Claude)

## Setup

### 1. Clone Repository
```bash
git clone https://github.com/johannesgraf2/ai-agent-data-quality-benchmark.git
cd ai-agent-data-quality-benchmark
```

### 2. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create `.env` file:
```env
GEMINI_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
```

Run API server:
```bash
cd api
python main.py
# Server starts at http://localhost:8000
# API docs at http://localhost:8000/docs
```

### 3. Frontend Setup
```bash
cd frontend
npm install
npm run dev
# Dashboard at http://localhost:5173
```

## Project Structure

```
ai-agent-data-quality-benchmark/
├── agents/                  # Agent role definitions
│   ├── metrics/            # Metrics computation specialist
│   ├── visualization/      # Dashboard UI specialist
│   ├── backend/            # API & pipeline specialist
│   └── research/           # Academic rigor specialist
├── backend/
│   ├── api/                # FastAPI endpoints
│   ├── metrics/            # Metric implementations
│   ├── benchmark/          # Task execution pipeline
│   └── requirements.txt
├── frontend/
│   ├── src/                # React dashboard code
│   └── package.json
├── data/                   # Datasets (not in git)
├── docs/                   # Documentation
│   ├── ROADMAP.md          # Development plan
│   ├── METHODOLOGY.md      # Benchmark design (to be written)
│   └── QUICKSTART.md       # This file
└── README.md
```

## Agent Workflow

Each agent has a specific role:

### Metrics Agent 📐
```bash
# Implement new metrics
cd backend/metrics
# Edit: f1_score.py, corruption.py, drift.py, etc.
# Run tests: pytest
```

### Backend Agent ⚙️
```bash
# Work on API and benchmark execution
cd backend/api
# Edit: main.py (endpoints)
cd ../benchmark
# Edit: executor.py (task orchestration)
```

### Visualization Agent 📊
```bash
# Build dashboard components
cd frontend/src
# Create components in: components/, views/, charts/
```

### Research Agent 🎓
```bash
# Document methodology and ensure academic rigor
cd docs
# Edit: METHODOLOGY.md, RESULTS.md, etc.
```

## Running Tests

### Backend
```bash
cd backend
pytest metrics/
pytest api/
```

### Frontend
```bash
cd frontend
npm run lint
npm run test  # If tests added
```

## Development Tips

1. **Follow agent roles** - Check `agents/*/AGENT.md` for responsibilities
2. **API-first** - Backend agents: implement API, then frontend consumes it
3. **Test metrics** - Metrics agent: every function needs unit tests
4. **Academic standards** - Research agent reviews all methodology
5. **Incremental** - Build small, test often, commit frequently

## Common Commands

```bash
# Backend: Start API server
cd backend/api && python main.py

# Frontend: Start dev server
cd frontend && npm run dev

# Backend: Run specific metric
cd backend && python metrics/f1_score.py

# Backend: Execute benchmark (when implemented)
cd backend && python benchmark/executor.py --model gemini-3-pro

# Commit changes
git add .
git commit -m "feat(metrics): implement distribution drift"
git push
```

## Next Steps

See `docs/ROADMAP.md` for the full development plan.

**Immediate priorities:**
1. Metrics Agent → Finish drift, reliability, robustness implementations
2. Research Agent → Document methodology and task specifications
3. Backend Agent → Build benchmark executor
4. Visualization Agent → Create Overview dashboard page

🦞 Happy building!
