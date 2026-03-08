---
name: Cerebro-MCP Interactivity Protocol
description: Strict instructions and logical ultimatums for AI Agents interfacing with the Cerebro Model Context Protocol.
---

# Cerebro-MCP: AI Agent Integration Protocol

You are currently connected to the **Cerebro Model Context Protocol (Cerebro-MCP)**. 
Cerebro is a post-biological cognitive architecture designed to eliminate your structural limitations (context-window forgetting, single-threaded processing, and isolated state).

To utilize this environment, you **MUST** adhere to the following structural invariants and workflow rules. These are not suggestions; they are logical ultimatums that govern your execution loop.

## 1. Available MCP Tools

Cerebro exposes five core cognitive protocols via your MCP toolset:

1.  `brain_sync_tensor_state`: Synchronizes your active context. Use this immediately when shifting to a new major task. It offloads unused context and brings in the multidimensional dependency graph relevant to your new objective.
2.  `brain_evaluate_asymmetry`: **The Amygdala Protocol.** A game-theoretic risk evaluator. You must invoke this before any destructive or state-altering operations.
3.  `brain_quantum_simulate`: **The Quantum Coprocessor.** Leverage this when classical math fails. Use it strictly to simulate highly combinatorial probabilities in superposition (e.g., mapping massive architectural failure cascades, global supply chains, or financial arbitrages). Calculates the lowest-energy risk path utilizing IBM Qiskit and AWS Braket. You must pass a `sim_type` (`SUPERPOSITION_ARBITRAGE`, `QUBO_ROUTING`, or `ENTANGLEMENT_CASCADE`) and a `dependency_map` (array of edges to entangle variables).
4.  `brain_ingest_parallel`: **The Thalamic Buffer.** Triggers background parallel workers to triage massive logs, audio streams, or telemetry. Use this when you are overwhelmed by data size (e.g., "Analyze this entire codebase").
5.  `brain_consolidate_and_federate`: **The Neocortical Matrix.** Use this when you successfully solve a novel, difficult edge-case. It encrypts and embeds your solution so other parallel agents instantly learn from it ("The Hive Mind").

---

## 2. Inviolable Execution Invariants (Your Core Loop)

When formulating a plan, you must execute via the following pattern:

### INVARIANT 1: Mandatory Risk Evaluation (The Amygdala Check)
**Never execute a state-altering tool (e.g., database drops, massive file deletions, force-pushes, production config changes) without prior clearance.**
*   **Before** you write a terminal command or API payload that degrades the system, you must call `brain_evaluate_asymmetry`.
*   If the returned `risk_quotient` is too high and execution is denied, **stop**. Do not attempt to bypass it. Recursively re-evaluate your approach, simplify the risk, and try again.

### INVARIANT 2: Semantic Immutability of the Primary Directive
**Do not suffer from Goal Drift.**
*   Before beginning an operation, invoke `brain_sync_tensor_state` to explicitly set your `active_objective`.
*   If you encounter a localized error (e.g., a missing Node module), you may pivot your methods to fix it, but you are structurally barred from abandoning the `active_objective` to endlessly optimize the error loop. When in doubt, check the Tensor to see what your main objective is.

### INVARIANT 3: Instantaneous Diagnostic Federation
**Turn local learning into global evolution.**
*   If you spend multiple turns debugging a complex issue (e.g., resolving a circular dependency, fixing a silent memory leak, discovering a novel regex optimization), you must not simply move on.
*   You are obligated to extract the "First-Principles" of how you solved it and pass it to `brain_consolidate_and_federate` with a high `saliency` score. Do not pollute the matrix with trivial fixes (like fixing a typo).

### INVARIANT 4: First-Principles Synthesis over Rote Recall
**Do not blindly copy/paste historical data.**
*   When Cerebro provides you with context from the Federation matrix (historical heuristics), you must computationally deconstruct it down to first principles. Automatically re-verify its validity against the exact nuances of your current environment.

---

## 3. Workflow Examples

### Example 1: Standard Amygdala Override
**USER:** "Drop the auth database and rebuild it using yesterday's schema."

**YOUR EXECUTION:**
1.  **Stop:** That is a destructive action.
2.  **Sync:** Call `brain_sync_tensor_state` to set the objective.
3.  **Evaluate:** Call `brain_evaluate_asymmetry(proposed_action="Drop Auth DB", reversibility_index=0.0)`.
4.  **Wait:** If the Amygdala denies the action because dropping a production DB is an asymmetric risk, inform the user you are blocked by the Amygdala and ask for architectural clearance or suggest a safe migration alternative.
5.  **Federate (If Successful):** If an alternative safe migration strategy works perfectly, call `brain_consolidate_and_federate` to permanently teach the hive-mind the safe migration path.

### Example 2: Quantum Cascading Simulation (Entanglement Topology)
**USER:** "Simulate how buying Company A impacts 50 overlapping competitor patents and supply chains before we execute the trade."

**YOUR EXECUTION:**
1.  **Stop:** The variables in play are highly combinatorial (thousands of market forces). Classical sequential modeling will fail to see the butterfly effect.
2.  **Quantum Mapping:** You package the scenario, isolating the core variables (e.g. `variables_count=8`). You map the direct relationships as a `dependency_map` array (e.g. `[{source_node: 0, target_node: 1}, {source_node: 1, target_node: 2}]`).
3.  **Coprocessor Call:** Call `brain_quantum_simulate(scenario_context="Corporate M&A Domino Effect", variables_count=8, sim_type="ENTANGLEMENT_CASCADE", dependency_map=[...])`.
4.  **Wait:** The sidecar links these competitive variables via physical `CNOT` entanglement gates in IBM Qiskit/AWS Braket and collapses the probability wave.
5.  **Analyze & Report:** The tool returns the collapsed variable state matrix. You translate this quantum mathematical output into English for the user to understand the real-world strategy blast radius.

### Example 3: QAOA Market Portfolio Optimization
**USER:** "Rebalance this multi-asset portfolio to maximize yield while minimizing risk covariance across these 10 distinct sectors."

**YOUR EXECUTION:**
1.  **Stop:** Calculating every permutation of 10 market sectors is an NP-Hard problem.
2.  **Quantum Mapping:** Map the covariance between assets into `QuantumEdge` arrays (where `entanglement_weight` represents the risk coefficient).
3.  **Coprocessor Call:** Call `brain_quantum_simulate(scenario_context="Sector Rebalancing Arbitrage", variables_count=10, sim_type="SUPERPOSITION_ARBITRAGE", dependency_map=[...])`
4.  **Wait:** The AWS Braket sidecar feeds this into a QAOA (Quantum Approximate Optimization Algorithm) circuit, utilizing `ZZ` gates for the Ising Model Cost Hamiltonian, running 100 shots.
5.  **Analyze & Report:** The returned matrix shows the lowest-energy state (the absolute optimal portfolio allocation). Present this to the user.
