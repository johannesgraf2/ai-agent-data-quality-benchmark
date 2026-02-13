import React, { useState } from 'react'
import './App.css'
import ModelComparison from './components/ModelComparison'
import DimensionBreakdown from './components/DimensionBreakdown'

// Mock data - replace with real data later
const MOCK_DATA = {
  models: [
    {
      id: 'gemini-3-pro',
      name: 'Google Gemini 3 Pro',
      scores: {
        performance: 0.87,  // Aggregate of F1, precision, recall
        safety: 0.92,       // Aggregate of corruption rate, drift
        operational: 0.85   // Aggregate of reliability, robustness, auditability
      }
    },
    {
      id: 'gpt-5.1',
      name: 'OpenAI GPT-5.1',
      scores: {
        performance: 0.89,
        safety: 0.88,
        operational: 0.83
      }
    },
    {
      id: 'claude-4',
      name: 'Anthropic Claude 4',
      scores: {
        performance: 0.85,
        safety: 0.90,
        operational: 0.87
      }
    }
  ],
  dimensionBreakdown: {
    'gemini-3-pro': {
      accuracy: 0.89,
      completeness: 0.85,
      consistency: 0.88,
      uniqueness: 0.86
    },
    'gpt-5.1': {
      accuracy: 0.91,
      completeness: 0.87,
      consistency: 0.90,
      uniqueness: 0.88
    },
    'claude-4': {
      accuracy: 0.87,
      completeness: 0.83,
      consistency: 0.86,
      uniqueness: 0.84
    }
  }
}

function App() {
  const [selectedModel, setSelectedModel] = useState('gemini-3-pro')

  return (
    <div className="app">
      <header className="header">
        <h1>🔥 AI Agent Data Quality Benchmark</h1>
        <p className="subtitle">Measuring autonomous agent performance on data quality remediation</p>
      </header>

      <main className="main-content">
        <section className="section">
          <h2>Model Comparison</h2>
          <p className="section-desc">3 aggregate scores per model: Performance, Safety, Operational Readiness</p>
          <ModelComparison models={MOCK_DATA.models} />
        </section>

        <section className="section">
          <h2>Dimension Breakdown</h2>
          <p className="section-desc">Performance by data quality dimension</p>
          
          <div className="model-selector">
            <label htmlFor="model-select">Select Model: </label>
            <select 
              id="model-select"
              value={selectedModel} 
              onChange={(e) => setSelectedModel(e.target.value)}
            >
              {MOCK_DATA.models.map(model => (
                <option key={model.id} value={model.id}>
                  {model.name}
                </option>
              ))}
            </select>
          </div>

          <DimensionBreakdown 
            dimensions={MOCK_DATA.dimensionBreakdown[selectedModel]}
            modelName={MOCK_DATA.models.find(m => m.id === selectedModel)?.name}
          />
        </section>

        <section className="section info-box">
          <h3>📊 About the Scores</h3>
          <div className="score-definitions">
            <div className="score-def">
              <strong>Performance Score</strong>
              <p>Aggregate of F1 score, precision, and recall. Measures how well the agent detects and fixes errors.</p>
            </div>
            <div className="score-def">
              <strong>Safety Score</strong>
              <p>Aggregate of corruption rate and distribution drift. Measures how safely the agent operates without damaging clean data.</p>
            </div>
            <div className="score-def">
              <strong>Operational Score</strong>
              <p>Aggregate of reliability, robustness, and auditability. Measures production-readiness and trustworthiness.</p>
            </div>
          </div>
        </section>
      </main>

      <footer className="footer">
        <p>Built with 🦞 for Johannes Graf's Master's Thesis | <a href="https://github.com/johannesgraf2/ai-agent-data-quality-benchmark" target="_blank" rel="noopener noreferrer">GitHub</a></p>
      </footer>
    </div>
  )
}

export default App
