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
        logging.info(f"🌌 Quantum Delegation: Simulating {request.variables_count}-variable probability cascade for: {request.scenario_context}")
        
        # The number of variables maps directly to the required Qubits.
        qubits = min(request.variables_count, 10) # Caps at 10 for basic testing limits
        
        if self.provider == "AWS_BRAKET":
            prob, selected_path = self._run_aws_braket(qubits)
        else:
            prob, selected_path = self._run_qiskit_simulator(qubits)
            
        logging.info(f"🌌 Quantum Collapse: Lowest Energy Probability {prob:.4f} | Path: {selected_path}")
        
        return cerebro_pb2.QuantumResponse(
            lowest_energy_probability=prob,
            optimized_path=selected_path
        )
        
    def _run_qiskit_simulator(self, num_qubits):
        """ Runs a QAOA-style superposition on IBM Qiskit (or local Aer simulator) """
        circuit = QuantumCircuit(num_qubits, num_qubits)
        
        # 1. Place all potential architectural states into a uniform superposition
        for q in range(num_qubits):
            circuit.h(q)
            
        # 2. Simulate entanglement/interference representing dependencies between failure states
        if num_qubits > 1:
            circuit.cx(0, 1)

        # 3. Measurement (Collapsing the probability wave)
        circuit.measure(range(num_qubits), range(num_qubits))
        
        simulator = AerSimulator()
        job = simulator.run(circuit, shots=1)
        result = job.result().get_counts()
        
        measured_state = list(result.keys())[0]
        # Calculate a naive probability risk factor from the state
        probability = measured_state.count("1") / num_qubits if num_qubits > 0 else 0.0
        
        return probability, f"state=|{measured_state}>"

    def _run_aws_braket(self, num_qubits):
        """ Runs the superposition circuit directly on AWS Braket infrastructure """
        logging.info("🌌 Connecting to AWS Braket SV1 Simulator...")
        circuit = BraketCircuit()
        
        # Superposition
        for q in range(num_qubits):
            circuit.h(q)
            
        # Simulated Entanglement
        if num_qubits > 1:
            circuit.cnot(0, 1)
            
        # In actual deployment, we would swap SV1 with 'arn:aws:braket:::device/qpu/rigetti/Aspen-M-3' for real hardware
        device = AwsDevice("arn:aws:braket:::device/quantum-simulator/amazon/sv1")
        task = device.run(circuit, shots=1)
        result = task.result()
        
        measurements = result.measurements[0]
        state_str = "".join(str(bit) for bit in measurements)
        probability = state_str.count("1") / num_qubits if num_qubits > 0 else 0.0
        
        return probability, f"aws-state=|{state_str}>"

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
