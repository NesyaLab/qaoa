#------------------------------------------------------------------------------
# config.py
#
# Configuration file
#
# © Leonardo Lavagna 2024
# @ NESYA https://github.com/NesyaLab
#------------------------------------------------------------------------------


from qiskit_aer import Aer


#num_graphs (int): The number of graph instances to be considered
num_graphs = 16

#p (int): The number of qaoa layers.
p = 2

#idx (int): An index between 0 and 15 that allows to select a graph instance from the data directory.
idx = 0

#seed (int): A seed for the pseudorandom generators (needed for reproducibility).
seed = 121

#shots (int): Number of measurements of each quantum circuit executed.
shots = 1024

#verbose (bool): A boolean variable that allows to work in debugging mode if True.
verbose = False

#backend (Qiskit backend): A Qiskit backend to simulate a quantum device.
backend = Aer.get_backend("aer_simulator")

#mixer (str): Type of qaoa mixer operator. Currently are available 'x', 'y', 'xx', 'xy' and 'yy' mixers.
mixer = "x" 

#method (str): Type of optimization method to be used with `scipy.optimize.minimize`. Available 'BFGS', 'L-BFGS-B', 'COBYLA' and 'SLSQP'.
method = 'COBYLA' 