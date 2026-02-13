import React from 'react'
import './ModelComparison.css'

function ModelComparison({ models }) {
  const getScoreColor = (score) => {
    if (score >= 0.9) return 'excellent'
    if (score >= 0.8) return 'good'
    if (score >= 0.7) return 'fair'
    return 'poor'
  }

  const formatScore = (score) => (score * 100).toFixed(1) + '%'

  return (
    <div className="model-comparison">
      {models.map(model => (
        <div key={model.id} className="model-card">
          <h3 className="model-name">{model.name}</h3>
          
          <div className="scores-grid">
            <div className="score-item">
              <div className="score-label">Performance</div>
              <div className={`score-value ${getScoreColor(model.scores.performance)}`}>
                {formatScore(model.scores.performance)}
              </div>
              <div className="score-bar">
                <div 
                  className={`score-fill ${getScoreColor(model.scores.performance)}`}
                  style={{ width: formatScore(model.scores.performance) }}
                />
              </div>
            </div>

            <div className="score-item">
              <div className="score-label">Safety</div>
              <div className={`score-value ${getScoreColor(model.scores.safety)}`}>
                {formatScore(model.scores.safety)}
              </div>
              <div className="score-bar">
                <div 
                  className={`score-fill ${getScoreColor(model.scores.safety)}`}
                  style={{ width: formatScore(model.scores.safety) }}
                />
              </div>
            </div>

            <div className="score-item">
              <div className="score-label">Operational</div>
              <div className={`score-value ${getScoreColor(model.scores.operational)}`}>
                {formatScore(model.scores.operational)}
              </div>
              <div className="score-bar">
                <div 
                  className={`score-fill ${getScoreColor(model.scores.operational)}`}
                  style={{ width: formatScore(model.scores.operational) }}
                />
              </div>
            </div>
          </div>
        </div>
      ))}
    </div>
  )
}

export default ModelComparison
