import React from 'react'
import './ModelComparison.css'

const METRICS = [
  { key: 'performance', label: 'Performance', className: 'performance' },
  { key: 'safety', label: 'Safety', className: 'safety' },
  { key: 'operational', label: 'Operational', className: 'operational' }
]

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
            <div className="model-label">{model.name}</div>
          </div>
        ))}
      </div>
    </div>
  )
}

export default ModelComparison
