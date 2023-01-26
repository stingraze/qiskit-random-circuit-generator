#(C)Tsubasa Kato - Inspire Search Corporation 1/26/2023 16:17PM
from qiskit import QuantumCircuit, assemble, Aer
from qiskit.circuit.random import random_circuit
sim = Aer.get_backend('aer_simulator')
x = 1
#Create 10 random quantum circuits
while (x < 11):
    print("Count:" + str(x))
    circ = random_circuit(2, 2, measure=True)
    print(circ)
    x = x + 1