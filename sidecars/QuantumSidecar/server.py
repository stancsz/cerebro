import grpc
from concurrent import futures
import logging
import os

# Quantum computing libraries
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
# Braket libraries for AWS Quantum
from braket.aws import AwsDevice
from braket.circuits import Circuit as BraketCircuit
from braket.circuits.observables import Z
import numpy as np
import networkx as nx

# The compiled pb2 files will be generated from proto/cerebro.proto
import cerebro_pb2
import cerebro_pb2_grpc

class QuantumCoprocessorServicer(cerebro_pb2_grpc.CognitiveEngineServicer):
    def __init__(self):
        logging.info("🌌 Quantum Sidecar: Initializing Subatomic Coprocessor.")
        
        # Determine active cloud quantum provider (IBM vs AWS)
        self.provider = os.getenv("QUANTUM_PROVIDER", "LocalSim") # Default to local simulator for fast iterative testing
        
        logging.info(f"🌌 Quantum Sidecar: Active Provider set to [{self.provider}].")

    def QuantumSimulateScenario(self, request, context):
        sim_name = cerebro_pb2.SimulationType.Name(request.sim_type)
        logging.info(f"🌌 Quantum Delegation: Simulating {request.variables_count}-variable {sim_name} cascade.")
        
        qubits = min(request.variables_count, 10) # Caps at 10 for basic testing limits
        
        if self.provider == "AWS_BRAKET":
            prob, selected_path, collapsed_state = self._run_aws_braket(qubits, request.sim_type, request.dependency_map)
        else:
            prob, selected_path, collapsed_state = self._run_qiskit_simulator(qubits, request.sim_type, request.dependency_map)
            
        logging.info(f"🌌 Quantum Collapse: Lowest Energy Prob {prob:.4f} | Path: {selected_path}")
        
        return cerebro_pb2.QuantumResponse(
            lowest_energy_probability=prob,
            optimized_path=selected_path,
            collapsed_state_matrix=collapsed_state
        )
        
    def _run_qiskit_simulator(self, num_qubits, sim_type, dependency_map):
        """ Maps specific multi-disciplinary schemas to physical Qubits using QAOA / QUBO patterns """
        circuit = QuantumCircuit(num_qubits, num_qubits)
        
        # 1. Base Superposition (Mixer Hamiltonian)
        for q in range(num_qubits):
            circuit.h(q)
            
        # 2. Cost Hamiltonian (Mapping real-world variables to Quantum Ising/QUBO Model)
        if sim_type == cerebro_pb2.QUBO_ROUTING or sim_type == cerebro_pb2.SUPERPOSITION_ARBITRAGE:
            # In real Portfolio Optimization (Braket Examples), covariance between assets 
            # is mapped to zz-interactions (Ising Model).
            for edge in dependency_map:
                if edge.source_node < num_qubits and edge.target_node < num_qubits:
                    # RZ and RZZ gates simulate the cost/covariance matrix (Gamma/Beta params mocked)
                    circuit.cx(edge.source_node, edge.target_node)
                    circuit.rz(edge.entanglement_weight, edge.target_node)
                    circuit.cx(edge.source_node, edge.target_node)
                    
        elif sim_type == cerebro_pb2.ENTANGLEMENT_CASCADE:
            # Domino effect causality mathematically represented by direct CNOTs
            for edge in dependency_map:
                if edge.source_node < num_qubits and edge.target_node < num_qubits:
                    circuit.cx(edge.source_node, edge.target_node)

        # 3. Measurement (Collapsing the probability wave)
        circuit.measure(range(num_qubits), range(num_qubits))
        
        simulator = AerSimulator()
        job = simulator.run(circuit, shots=1)
        result = job.result().get_counts()
        
        measured_state = list(result.keys())[0] # The exact collapsed state (e.g. '01011')
        probability = measured_state.count("1") / num_qubits if num_qubits > 0 else 0.0
        
        # Generate the collapsed variables matrix to return to the AI
        matrix = {f"Var_{i}": float(val) for i, val in enumerate(reversed(measured_state))}
        
        return probability, f"state=|{measured_state}>", matrix

    def _run_aws_braket(self, num_qubits, sim_type, dependency_map):
        """ 
        Runs the QAOA/Superposition circuit directly on AWS Braket infrastructure.
        Mirrors the logic found in amazon-braket-examples for Portfolio Optimization.
        """
        logging.info("🌌 Connecting to AWS Braket SV1 Simulator...")
        circuit = BraketCircuit()
        
        # Superposition (QAOA Mixer)
        for q in range(num_qubits):
            circuit.h(q)
            
        # AWS Braket QAOA Cost Hamiltonian formulation
        if sim_type == cerebro_pb2.QUBO_ROUTING or sim_type == cerebro_pb2.SUPERPOSITION_ARBITRAGE:
            for edge in dependency_map:
                if edge.source_node < num_qubits and edge.target_node < num_qubits:
                    # Braket ZZ-Gate represents the QUBO weights (covariance in finance, latency in routing)
                    circuit.zz(edge.source_node, edge.target_node, edge.entanglement_weight)
                    
        elif sim_type == cerebro_pb2.ENTANGLEMENT_CASCADE:
            for edge in dependency_map:
                if edge.source_node < num_qubits and edge.target_node < num_qubits:
                    circuit.cnot(edge.source_node, edge.target_node)
            
        # In actual deployment, we would swap SV1 with 'arn:aws:braket:::device/qpu/ionq/Aria-1' for real hardware
        device = AwsDevice("arn:aws:braket:::device/quantum-simulator/amazon/sv1")
        task = device.run(circuit, shots=100) # 100 shots to correctly find the energy minimums
        result = task.result()
        
        # Find the most frequent bitstring (lowest energy state for the QUBO problem)
        measurement_counts = result.measurement_counts
        best_state_str = measurement_counts.most_common(1)[0][0]
        
        # Probability translates to the risk safety factor
        probability = best_state_str.count("1") / num_qubits if num_qubits > 0 else 0.0
        
        matrix = {f"Var_{i}": float(val) for i, val in enumerate(best_state_str)}
        
        return probability, f"aws-state=|{best_state_str}>", matrix

    # We stub out the remaining gRPC endpoints since this sidecar strictly handles the Quantum features.
    def EvaluateRiskQuotient(self, request, context): pass
    def EmbedHeuristic(self, request, context): pass
    def PruneContextGraph(self, request, context): pass
    def ExtractSemantics(self, request, context): pass


def serve():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")
    # Bind to gRPC threads
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    cerebro_pb2_grpc.add_CognitiveEngineServicer_to_server(QuantumCoprocessorServicer(), server)
    
    port = '[::]:50052' # Running on a different port than the main Python Sidecar
    server.add_insecure_port(port)
    logging.info(f"Quantum Coprocessor Sidecar active on {port}. Awaiting entanglement...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
