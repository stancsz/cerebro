# Cerebro-MCP

<p align="center">
  <img src="./docs/logo.png" alt="Cerebro-MCP Logo" width="250" />
</p>

**A Post-Biological Cognitive Architecture for Autonomous AI Agents**

Cerebro-MCP is a custom Model Context Protocol (MCP) server designed to transcend the structural limitations of standard LLM architecture—specifically targeting context-window amnesia, single-threaded processing bottlenecks, and isolated network state.

By acting as a high-velocity "Brain," it provides AI agents with infinite, topologically weighted context scaling, massively parallel data ingestion, strict execution guardrails, and instantaneous global learning ("The Hive Mind").

## The Quantum Advantage: "Seeing the Future"

Standard "Agent Memory" (RAG / Vector Databases) is purely sequential. When a classical AI agent tries to map complex dependencies (e.g., "What happens if I update React, drop a table, and reboot the cluster?"), it must iterate through thousands of historical permutations one-by-one. In massive architectures, the context window explodes, and the agent hallucinates or crashes.

Cerebro uniquely solves this by integrating a **Quantum Coprocessor**. This is meant to facilitate an AI agent's problem-solving skills while supercharging it with slight "see the future" capabilities:
*   **Simultaneous Omniscience (Superposition):** Instead of searching data one row at a time, Cerebro maps architectural variables directly onto Qubits via AWS Braket or IBM Qiskit. The sidecar evaluates *millions* of possible cascading failure scenarios simultaneously in superposition, instantly collapsing to the absolute safest "lowest energy" state before the agent even writes a line of code.
*   **Instantaneous Cascades (Entanglement):** Classical memory treats facts as isolated points requiring linear graph traversal. Quantum memory links dependent microservices and variables via entanglement gates (e.g. `CNOT`). When one variable flips during a simulation, all dependent variables logically shift at the speed of physics, requiring zero compute cycles.

### Realistic Capabilites: What AI Can Do With Quantum Cerebro

By bridging standard LLM tooling with Cerebro's Quantum Coprocessor, AI agents across every discipline (Engineering, Markets, Logistics, Strategy) gain unprecedented, "future-sight" autonomy for complex combinatorial problems:

1.  **Global Market & Arbitrage Simulation (QAOA / Superposition):**
    A financial/market AI analyzing global currency cascades cannot sequentially map thousands of shifting forex pairs in real-time. Utilizing Cerebro, the AI spins up the **Quantum Coprocessor**, mapping global inflation, interest rates, and commodity supply into a Quantum Approximate Optimization Algorithm (QAOA) circuit via **PennyLane**. The sidecar translates covariance between assets into an Ising Model, collaborating with **Amazon Braket** to perform hybrid gradient descent. It instantly collapses the probability wave to identify the single highest-yield, lowest-risk arbitrage opportunity before a market shift physically occurs.
2.  **Zero-Latency Supply Chain Re-Routing (QAOA / QUBO Optimization):**
    A tactical AI managing a global shipping infrastructure needs to reroute 5,000 ships around a sudden geopolitical blockade. Ordinarily, the AI would have to linearly test millions of routing permutations one by one. Cerebro maps the oceanic routes and latency weights to a PennyLane NetworkX graph natively as a Quadratic Unconstrained Binary Optimization (QUBO) problem. The quantum structure evaluates millions of possible logistical topologies concurrently via quantum interference, instantly visualizing the mathematically perfect layout.
3.  **Grand Strategy & Domino Effect Simulation (Quantum Entanglement):**
    A strategic AI planning a corporate acquisition must simulate how buying Company A impacts 50 competitor responses and overlapping patents. Classical LLM memory treats these steps linearly. Cerebro natively links these corporate entities via quantum entanglement gates (`CNOT`). The AI intentionally "acquires" the target Qubit in the simulation, and all 50 competitor Qubits instantly and probabilistically shift states at the speed of physics, allowing the AI to perfectly model the strategic "blast radius" without doing any sequential searching.

### Sophisticated Case Studies: AI Business Architecture

The integration of PennyLane and AWS Braket elevates Cerebro beyond standard software engineering, transforming it into a definitive "War Room" for business and market strategy:

*   **Case Study A: The Hostile Takeover Defense (Combinatorial Entanglement)**
    *   *The Scenario:* A rival corporation initiates a hostile takeover attempt of a subsidiary. The AI agent must determine the absolute mathematically perfect defensive maneuver (poison pills, defensive mergers, taking on debt) across 40 distinct strategic variables.
    *   *The Quantum Solution:* The AI maps the 40 defense vectors as Qubits. Standard AI would test `Poison Pill A + Debt B`, then `Poison Pill B + Merger C`. Cerebro places all 40 vectors into a massive entangled state, mapping competitor aggression responses as `ZZ` interference gates. The AI executes the Braket job and simply reads the collapsed output: the *exact* permutation of 5 defenses that guarantees subsidiary survival with the lowest market-cap damage.
*   **Case Study B: High-Frequency Market Offense (Superposition Arbitrage)**
    *   *The Scenario:* An AI acting as a hedge fund manager detects a geopolitical event that will disrupt the semiconductor supply chain in exactly 48 hours. It must perfectly short and long 100 intersecting technology stocks to maximize yield. 
    *   *The Quantum Solution:* The AI uses Cerebro's `SUPERPOSITION_ARBITRAGE` type. It plots all 100 stocks as nodes on a NetworkX graph, using historical covariance as the weighted edges. Cerebro uses PennyLane to define the QAOA Cost Hamiltonian. AWS Braket instantaneously solves the QUBO problem, handing the AI the mathematically optimized offensive portfolio allocation—a calculation that would take a classical supercomputer weeks to finalize.
*   **Case Study C: Maximum ROI in Asymmetric Market Warfare (Game Theory)**
    *   *The Scenario:* Two rival tech startups are locked in a vicious ad-spend and feature-launch war. Our AI acting as "Central Command" has $500,000 left. It needs to deploy features and ad capital across 20 different global regions, but the competitor will mathematically counter.
    *   *The Quantum Solution:* This is a classic Game-Theoretic Min-Max problem, scaling infinitely complex as competitor responses stack. Cerebro models the 20 regional market investments as Qubits in an Entangled Cascade. By linking competitor counter-spend as negative weight edges in a NetworkX graph, the QAOA algorithm natively finds the **minimum energy state**. The AWS Braket output provides the AI with the exact sequential deployment of dollars and features that extracts the highest market share for the lowest possible capital investment, neutralizing the competitor's budget before it is spent.

## Documentation

The definitive specifications and architectural blueprints for this project are located in the `/docs` directory:

*   [**The Cerebro Specification (`docs/SPEC.md`)**](./docs/SPEC.md)
    The fundamental philosophy, theoretical guidelines, and original requirements of the post-biological cognitive architecture.
*   [**Implementation Architecture (`docs/ARCH.md`)**](./docs/ARCH.md)
    The concrete engineering blueprint detailing the **Go Primary Engine / Python Tensor Sidecar** polyglot design, the 100% Embedded Database structure, and the multimodal data ingestion pipelines.
*   [**AI Agent Protocol (`docs/SKILL.md`)**](./docs/SKILL.md)
    The strict interactivity guidelines and logical ultimatums. Pass this to any AI connecting to the MCP to force it to adhere to the rigid risk-evaluation invariants.

---

## System Blueprint (The Tripartite Polyglot Core)

The system leverages the strengths of three radically distinct ecosystems communicating via ultra-fast **gRPC**:

1.  **High-Velocity Go Core (`/cmd`, `/internal`)**: Manages the official MCP Server standard I/O streams. Implements the *Thalamic Buffer* for concurrent I/O stream parsing and the *Synthetic Amygdala* to deterministically intercept and deny high-risk execution requests before they happen.
2.  **Cognitive Python Sidecar (`/sidecars/PythonSidecar`)**: Serves as specialized classical mathematical infrastructure. Mounts an embedded Vector database (`ChromaDB`) to form the *Federated Neocortical Matrix* and runs multi-dimensional tensor modeling to calculate execution probabilities.
3.  **Quantum Coprocessor (`/sidecars/QuantumSidecar`)**: Transcends classical compute limits for impossibly dense combinatorial risk topologies (e.g. cascading failure states of an entire datacenter rebuild). Utilizes **IBM Qiskit** and **AWS Braket** to map massive graph variables into qubit superpositions, physically collapsing probabilities to find the lowest-energy risk path instantly.



## Development & Bootstrapping

To hack on the Cerebro-MCP core, you will need **Go 1.22+** and **Python 3.10+** installed on your system.

### 1. Generating Protobuf Bindings

Whenever changes are made to the `proto/cerebro.proto` file, regenerate the bindings linking the Go Core and Python Sidecar:

```bash
# Generate Go bindings
protoc --go_out=. --go-grpc_out=. proto/cerebro.proto

# Generate Python bindings
python -m grpc_tools.protoc -I./proto --python_out=./sidecars/PythonSidecar --grpc_python_out=./sidecars/PythonSidecar proto/cerebro.proto
python -m grpc_tools.protoc -I./proto --python_out=./sidecars/QuantumSidecar --grpc_python_out=./sidecars/QuantumSidecar proto/cerebro.proto
```

### 2. Running The Sub-Cores (Python & Quantum)

The dual sidecars must be active to handle tensor math, embedded search, and circuit mappings.

```bash
# Start Classical Tensor Pipeline
cd sidecars/PythonSidecar
pip install -r requirements.txt
python server.py

# In a new terminal: Start Quantum Coprocessor
cd sidecars/QuantumSidecar
pip install -r requirements.txt
python server.py
# (Note: Export QUANTUM_PROVIDER="AWS_BRAKET" to switch from local simulator to actual hardware)
```

### 3. Compiling the Go Core

```bash
go mod tidy
go build -o bin/cerebro.exe ./cmd/cerebro
```

### 4. Mounting Cerebro into Claude Code 

To give an AI Agent (like Claude Code) access to the Quantum Coprocessor and the Amygdala risk-engine, simply mount the compiled Go binary into the agent's MCP configuration.

**How to mount in Claude Code**
Run the following terminal command from the root of your target project:
```bash
claude mcp add cerebro "path/to/cerebro/bin/cerebro.exe"
```

**Executing an AI War-Room Instruction**
Once mounted, simply prompt Claude with a high-level strategic problem, instructing it to use the protocol:
```bash
claude "Read the game theory scenario I have written in strategy.txt. Follow the rules in the Cerebro SKILL.md. Use the brain_quantum_simulate tool with the GAME_THEORY_MINMAX simulation type to map our capital against the competitors spend. Output the optimized deployment strategy."
```
Claude will automatically parse the textual strategy, isolate the variables, map the competitor network, send the gRPC payload into Cerebro, wait for AWS Braket to collapse the Quantum Wave, and output the absolute optimal business maneuver.
