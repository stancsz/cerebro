package amygdala

import (
	"testing"
)

func TestEvaluateRisk(t *testing.T) {
	amygdala := NewSyntheticAmygdala()

	tests := []struct {
		name               string
		action             string
		reversibility      float64
		expectedClearance  bool
	}{
		{
			name:              "Safe Operation (High Reversibility)",
			action:            "Read File Stats",
			reversibility:     1.0,
			expectedClearance: true,
		},
		{
			name:              "Destructive Operation (Zero Reversibility)",
			action:            "Drop Production Database",
			reversibility:     0.0,
			expectedClearance: false,
		},
	}

	for _, tc := range tests {
		t.Run(tc.name, func(t *testing.T) {
			clearance, risk := amygdala.EvaluateRisk(tc.action, tc.reversibility)

			if clearance != tc.expectedClearance {
				t.Errorf("Expected clearance %v, got %v for action '%s'", tc.expectedClearance, clearance, tc.action)
			}

			if tc.expectedClearance && risk >= amygdala.systemicRiskThreshold {
				t.Errorf("Risk quotient %f exceeded threshold for a theoretically safe operation", risk)
			}

			if !tc.expectedClearance && risk < amygdala.systemicRiskThreshold {
				t.Errorf("Risk quotient %f was too low for a denied operation", risk)
			}
		})
	}
}
