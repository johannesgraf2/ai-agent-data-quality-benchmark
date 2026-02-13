# 🔥 AI Agent Data Quality Benchmark Dashboard

A clean, focused dashboard for comparing AI agent performance on data quality tasks.

## 🎯 What This Shows

**3 Aggregate Scores per Model:**
1. **Performance** - How well the agent detects and fixes errors (F1, precision, recall)
2. **Safety** - How safely it operates without damaging clean data (corruption rate, drift)
3. **Operational** - Production readiness and trustworthiness (reliability, robustness, auditability)

**4 Dimension Scores:**
- Accuracy - Fixing factually wrong data
- Completeness - Filling missing values
- Consistency - Resolving contradictions
- Uniqueness - Removing duplicates

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/johannesgraf2/ai-agent-data-quality-benchmark.git
cd ai-agent-data-quality-benchmark
```

### 2. Run Frontend (Dashboard)
```bash
cd frontend
npm install
npm run dev
```

Dashboard opens at: **http://localhost:5173**

### 3. Run Backend API (Optional)
```bash
cd backend
pip install -r requirements.txt
cd api
python3 main.py
```

API runs at: **http://localhost:8000**
API docs at: **http://localhost:8000/docs**

## 📊 Current State

The dashboard is **fully functional** with **mock data**. It's ready to use for:
- Developing the UI
- Testing visualizations
- Presenting the concept

When you have real benchmark results (in a few months), plug them in using one of the methods in [`docs/DATA_INTEGRATION.md`](docs/DATA_INTEGRATION.md).

## 🎨 Features

- **Model Comparison Cards** - Side-by-side comparison of 3 scores per model
- **Dimension Breakdown** - Visual breakdown by data quality dimension
- **Color-Coded Scores** - Green (excellent), blue (good), yellow (fair), red (poor)
- **Responsive Design** - Works on desktop, tablet, mobile
- **Clean & Academic** - Professional styling suitable for thesis presentation

## 📂 Project Structure

```
/
├── frontend/            # React dashboard (Vite)
│   ├── src/
│   │   ├── App.jsx     # Main app with mock data
│   │   ├── components/ # ModelComparison, DimensionBreakdown
│   │   └── *.css       # Styling
│   └── package.json
├── backend/             # Python FastAPI (optional)
│   ├── api/            # REST endpoints
│   │   └── main.py    # 3 aggregate scores API
│   ├── metrics/        # Metric calculations (F1, corruption, drift)
│   └── requirements.txt
└── docs/
    ├── DATA_INTEGRATION.md  # How to plug in real data
    └── ROADMAP.md           # Development plan
```

## 🔧 Customization

### Change Mock Data
Edit `/frontend/src/App.jsx` lines 8-48 to update model scores.

### Add More Models
Add to the `models` array in `App.jsx`:
```javascript
{
  id: 'new-model-id',
  name: 'New Model Name',
  scores: {
    performance: 0.XX,
    safety: 0.XX,
    operational: 0.XX
  }
}
```

### Change Colors/Styling
Edit CSS files in `/frontend/src/*.css` and `/frontend/src/components/*.css`.

## 📖 Documentation

- **[DATA_INTEGRATION.md](docs/DATA_INTEGRATION.md)** - How to plug in real benchmark results
- **[ROADMAP.md](docs/ROADMAP.md)** - Development timeline (focus on dashboard only)
- **[QUICKSTART.md](docs/QUICKSTART.md)** - Detailed setup guide

## 🎓 Thesis Context

This dashboard supports Johannes Graf's master's thesis on AI agent data quality remediation, with focus on:
- Traditional ML metrics (F1, precision, recall)
- Safety metrics (corruption, drift)
- Novel operational readiness metrics (reliability, robustness, auditability)

## 🦞 Built With

- **Frontend:** React + Vite
- **Styling:** CSS3 (no framework, lightweight)
- **Backend:** FastAPI (Python) - optional
- **Charts:** Pure CSS progress bars (simple, effective)

## 📝 License

MIT License - see LICENSE file

---

**Repository:** https://github.com/johannesgraf2/ai-agent-data-quality-benchmark  
**Author:** Johannes Graf  
**Built with:** 🦞 Specialized AI agents
