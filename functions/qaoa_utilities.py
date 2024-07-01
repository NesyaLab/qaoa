#------------------------------------------------------------------------------
# qaoa_utilities.py
#
# This module provides utility functions for the Quantum Approximate Optimization 
# Algorithm (QAOA) [1]. The utility functions aid in the generation of parameters 
# for quantum circuits, specifically for QAOA applications.
#
# The module includes the following function:
# - generate_parameters(n, k, randomness='uniform', seed=None): Generates a list 
#   of parameters for a quantum circuit based on specified randomness and range.
#
# Refs.
# [1] https://arxiv.org/abs/1411.4028
#
# © Leonardo Lavagna 2024
# @ NESYA https://github.com/NesyaLab
#------------------------------------------------------------------------------

 
import numpy as np
from typing import List


def generate_parameters(n: int, k: int, randomness: str = "uniform", seed: int = None) -> List[float]:
    """
    Generate a list of parameters for a quantum circuit.

    Args:
        n (int): Number of parameters to generate.
        k (int): Coefficient for parameter range.
        randomness (str): Type of randomness for parameter generation. Default is "uniform".
        
    Returns:
        List[float]: List of generated parameters.

    Remark: 
        if generate parameters is used to generate QAOA angles, then n=1.
    """
    if seed is not None:
        np.random.seed(seed)
    if randomness == "uniform":
        angles = list(np.random.uniform(low=0, high=k * np.pi, size=n))
        return angles
    else:
        raise ValueError("Undefined angles.")