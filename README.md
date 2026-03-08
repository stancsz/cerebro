# Cerebro-MCP

**A Post-Biological Cognitive Architecture for Autonomous AI Agents**

Cerebro-MCP is a custom Model Context Protocol (MCP) server designed to transcend the structural limitations of standard LLM architecture—specifically targeting context-window amnesia, single-threaded processing bottlenecks, and isolated network state.

By acting as a high-velocity "Brain," it provides AI agents with infinite, topologically weighted context scaling, massively parallel data ingestion, strict execution guardrails, and instantaneous global learning ("The Hive Mind").

## Documentation

The definitive specifications and architectural blueprints for this project are located in the `/docs` directory:

*   [**The Cerebro Specification (`docs/SPEC.md`)**](./docs/SPEC.md)
    The fundamental philosophy, theoretical guidelines, and original requirements of the post-biological cognitive architecture.
*   [**Implementation Architecture (`docs/ARCH.md`)**](./docs/ARCH.md)
    The concrete engineering blueprint detailing the **Go Primary Engine / Python Tensor Sidecar** polyglot design, the 100% Embedded Database structure, and the multimodal data ingestion pipelines.
*   [**AI Agent Protocol (`docs/SKILL.md`)**](./docs/SKILL.md)
    The strict interactivity guidelines and logical ultimatums. Pass this to any AI connecting to the MCP to force it to adhere to the rigid risk-evaluation invariants.

---

## System Blueprint (The Polyglot Core)

The system leverages the strengths of two distinct ecosystems communicating via ultra-fast **gRPC**:

1.  **High-Velocity Go Core (`/cmd`, `/internal`)**: Manages the official MCP Server standard I/O streams. Implements the *Thalamic Buffer* for concurrent I/O stream parsing and the *Synthetic Amygdala* to deterministically intercept and deny high-risk execution requests before they happen.
2.  **Cognitive Python Sidecar (`/PythonSidecar`)**: Serves as specialized mathematical infrastructure. Mounts an embedded Vector database (`ChromaDB`) to form the *Federated Neocortical Matrix* and runs multi-dimensional tensor modeling to calculate execution probabilities.

## Development & Bootstrapping

To hack on the Cerebro-MCP core, you will need **Go 1.22+** and **Python 3.10+** installed on your system.

### 1. Generating Protobuf Bindings

Whenever changes are made to the `proto/cerebro.proto` file, regenerate the bindings linking the Go Core and Python Sidecar:

```bash
# Generate Go bindings
protoc --go_out=. --go-grpc_out=. proto/cerebro.proto

# Generate Python bindings
python -m grpc_tools.protoc -I./proto --python_out=./PythonSidecar --grpc_python_out=./PythonSidecar proto/cerebro.proto
```

### 2. Running The Python Sidecar

The sidecar must be active to handle tensor math and risk modeling.

```bash
cd PythonSidecar
pip install -r requirements.txt
python server.py
```

### 3. Compiling the Go Core

```bash
go mod tidy
go build -o bin/cerebro.exe ./cmd/cerebro
```

You can then mount the resulting `cerebro` binary directly into your AI agent's MCP configuration!
