package tensor

import (
	"reflect"
	"testing"
)

func TestTensorManager_SyncState(t *testing.T) {
	manager := NewTensorManager()

	initialObjective := "Refactor Core Loop"
	initialState := map[string]interface{}{
		"pid":  1234,
		"user": "root",
	}

	// First Sync
	manager.SyncState(initialObjective, initialState)

	if manager.ActiveObjective != initialObjective {
		t.Errorf("Expected ActiveObjective %s, got %s", initialObjective, manager.ActiveObjective)
	}

	currentContext := manager.GetCurrentContext()
	if !reflect.DeepEqual(currentContext, initialState) {
		t.Errorf("Expected environment %v, got %v", initialState, currentContext)
	}

	// Update State
	newObjective := "Debug Memory Leak"
	newStateDelta := map[string]interface{}{
		"pid":       5678,
		"core_dump": "/tmp/dump.core",
	}

	manager.SyncState(newObjective, newStateDelta)

	if manager.ActiveObjective != newObjective {
		t.Errorf("Expected ActiveObjective %s, got %s", newObjective, manager.ActiveObjective)
	}

	updatedContext := manager.GetCurrentContext()

	// Ensure merging worked
	if updatedContext["pid"] != 5678 {
		t.Errorf("Expected merged PID 5678, got %v", updatedContext["pid"])
	}

	if updatedContext["core_dump"] != "/tmp/dump.core" {
		t.Errorf("Expected core_dump map entry, got %v", updatedContext["core_dump"])
	}

	// Ensure old keys weren't deleted unless overwritten
	if updatedContext["user"] != "root" {
		t.Errorf("Expected retained user root, got %v", updatedContext["user"])
	}
}
