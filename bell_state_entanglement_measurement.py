from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.primitives import Sampler
from qiskit.visualization import plot_histogram # so we can display results
from IPython.display import display

# To begin we create the following circuit by sequentially adding gates from L to R
circuit = QuantumCircuit(2) # specify the number of circuits to be used
circuit.h(0)
circuit.s(0)
circuit.h(0)
circuit.t(0)
circuit.draw(output="mpl", filename="HSHT") #Note the circuit HSHT is printed in the terminal


### 2nd circuit using Hadamard and a controlled NOT gate with measurements
X = QuantumRegister(1, "X")
Y = QuantumRegister(1, "Y")
A = ClassicalRegister(1, "A")
B = ClassicalRegister(1, "B")
circuit = QuantumCircuit(Y, X, B, A)
circuit.h(Y) #Hadamard on Y
circuit.cx(Y,X) # Copy
circuit.measure(Y, B) #Measurement on Y to classical register B
circuit.measure(X, A) #Measurement on X to classical register A
circuit.draw(output="mpl", filename="hadamard controlled NOT")

# The circuit can be simulated using the Sampler primitive
results = Sampler().run(circuit).result()
stats = results.quasi_dists[0].binary_probabilities()
plot_histogram(stats, filename="Quasi-probability graph")
