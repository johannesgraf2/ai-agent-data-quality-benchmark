import React from 'react'
import './ModelComparison.css'
import geminiIcon from '../assets/gemini.svg'
import openaiIcon from '../assets/openai.svg'
import claudeIcon from '../assets/claude.svg'

const METRICS = [
  { key: 'performance', label: 'Performance', className: 'performance' },
  { key: 'safety', label: 'Safety', className: 'safety' },
  { key: 'operational', label: 'Operational', className: 'operational' }
]

const MODEL_ICONS = {
  'gemini-3-pro': geminiIcon,
  'gpt-5.1': openaiIcon,
  'claude-4': claudeIcon
}

function ModelComparison({ models }) {
  const formatScore = (score) => (score * 100).toFixed(1) + '%'

  return (
    <div className="comparison-chart">
      <div className="chart-legend">
        {METRICS.map(metric => (
          <div key={metric.key} className="legend-item">
            <span className={`legend-swatch ${metric.className}`} />
            {metric.label}
          </div>
        ))}
      </div>

      <div className="chart-body">
        {models.map(model => (
          <div key={model.id} className="chart-group">
            <div className="bars">
              {METRICS.map(metric => (
                <div key={metric.key} className="bar-wrapper">
                  <div
                    className={`bar ${metric.className}`}
                    style={{ height: `${model.scores[metric.key] * 100}%` }}
                  >
                    <span className="bar-value">{formatScore(model.scores[metric.key])}</span>
                  </div>
                </div>
              ))}
            </div>
            <div className="model-label">
              <img className="model-icon" src={MODEL_ICONS[model.id]} alt="" aria-hidden="true" />
              {model.name}
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

export default ModelComparison
