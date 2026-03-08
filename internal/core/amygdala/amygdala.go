package amygdala

import (
	"log"
)

// The Amygdala interceptor handles the strict probabilistic risk checks
// This is the middleware that MUST execute before any external tool is fired
type SyntheticAmygdala struct {
	// threshold determines when a proposed action should be immediately denied
	systemicRiskThreshold float64
}

func NewSyntheticAmygdala() *SyntheticAmygdala {
	return &SyntheticAmygdala{
		// 15% probability of destruction is the baseline cut-off
		systemicRiskThreshold: 0.15,
	}
}

// EvaluateRisk takes a struct outlining what an agent wants to do
// and calculates the mathematical probability of a system failure.
// Ideally, this calls the Python Sidecar to calculate historical success embeddings
func (a *SyntheticAmygdala) EvaluateRisk(proposedAction string, reversibilityIndex float64) (executionClearance bool, risk float64) {
	log.Printf("AMYGDALA INTERCEPTOR: Evaluating %s (Reversibility: %.2f)", proposedAction, reversibilityIndex)

	// Stub: In reality, make gRPC call to Python Sidecar Tensor Risk module
	// For testing, calculate a baseline naive score
	simulatedRiskScore := 0.05 // Safe default

	if reversibilityIndex == 0.0 { // Destructive (e.g. dropping a DB)
		simulatedRiskScore = 0.95
	}

	executionClearance = simulatedRiskScore < a.systemicRiskThreshold

	if !executionClearance {
		log.Printf("AMYGDALA DENIED EXECUTION: Risk quotient (%.2f) exceeds threshold (%.2f)", simulatedRiskScore, a.systemicRiskThreshold)
		return false, simulatedRiskScore
	}

	log.Printf("AMYGDALA APPROVED: Execution clearance granted (Risk: %.2f)", simulatedRiskScore)
	return true, simulatedRiskScore
}
