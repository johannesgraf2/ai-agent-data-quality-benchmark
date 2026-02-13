import React from 'react'
import './DimensionBreakdown.css'

function DimensionBreakdown({ dimensions, modelName }) {
  const formatScore = (score) => (score * 100).toFixed(1) + '%'

  const dimensionLabels = {
    accuracy: 'Accuracy',
    completeness: 'Completeness',
    consistency: 'Consistency',
    uniqueness: 'Uniqueness'
  }

  const dimensionIcons = {
    accuracy: '🎯',
    completeness: '📋',
    consistency: '🔗',
    uniqueness: '✨'
  }

  return (
    <div className="dimension-breakdown">
      <div className="dimensions-grid">
        {Object.entries(dimensions).map(([key, value]) => (
          <div key={key} className="dimension-card">
            <div className="dimension-icon">{dimensionIcons[key]}</div>
            <div className="dimension-label">{dimensionLabels[key]}</div>
            <div className="dimension-score">{formatScore(value)}</div>
            <div className="dimension-bar">
              <div 
                className="dimension-fill"
                style={{ width: formatScore(value) }}
              />
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

export default DimensionBreakdown
