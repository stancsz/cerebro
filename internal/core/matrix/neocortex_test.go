package matrix

import (
	"strings"
	"testing"
)

func TestMatrixConsolidateAndFederate(t *testing.T) {
	neocortex := NewNeocortex()

	t.Run("Reject Low Saliency Heuristics", func(t *testing.T) {
		_, err := neocortex.ConsolidateAndFederate("Fixed a spelling mistake in read me.", 80)
		if err == nil {
			t.Fatal("Expected error when saliency is below 90, but got nil")
		}
		if !strings.Contains(err.Error(), "below 90 baseline") {
			t.Errorf("Expected saliency error message, got: %v", err)
		}
	})

	t.Run("Accept High Saliency Heuristics", func(t *testing.T) {
		heuristic := "Invariant Rule: Prevent circular deps by loading X before Y."
		validationKey, err := neocortex.ConsolidateAndFederate(heuristic, 95)
		
		if err != nil {
			t.Fatalf("Expected nil error for high saliency, got: %v", err)
		}

		if validationKey == "" {
			t.Fatal("Validation key (cryptographic hash) was empty")
		}

		// Calculate expected hash length (SHA256 hex encoded is 64 characters)
		if len(validationKey) != 64 {
			t.Errorf("Expected 64-character hex hash, got %d chars: %s", len(validationKey), validationKey)
		}
	})
}
