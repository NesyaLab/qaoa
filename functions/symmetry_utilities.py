#------------------------------------------------------------------------------
# symmetry_utilities.py
#
# This module provides utility functions for computing graph symmetries using 
# the pynauty library [1]. The utilities help in analyzing the automorphisms, 
# symmetry generators, and orbits of a graph.
#
# The module includes the following functions:
# - get_number_of_automorphisms(G, adjacency_dict): Computes the number of 
#   automorphisms of a graph.
# - get_symmetry_generators(G, adjacency_dict): Computes the symmetry generators 
#   of a graph.
# - get_symmetry_orbits(G, adjacency_dict): Computes the orbits and the number 
#   of orbits of a graph.
#
# Refs
# [1] https://github.com/pdobsan/pynauty
#
# © Leonardo Lavagna 2024
# @ NESYA https://github.com/NesyaLab
#------------------------------------------------------------------------------


from typing import List, Tuple
from networkx import Graph
import numpy as np
from pynauty import *


def get_number_of_automorphisms(G: Graph, adjacency_dict: dict) -> int:
    """
    Compute the number of automorphisms of a graph G, using pynauty.
    
    Args:
        G (Graph): Input graph (created with the Problems class).
        adjacency_dict (dict): Adjacency dictionary of G.
    
    Returns:
        int: The cardinality of Aut(G).
    """
    N = G.get_number_of_nodes()
    g = Graph(N, directed=False, adjacency_dict=adjacency_dict)
    num_automorphisms = autgrp(g)[1]
    
    return int(num_automorphisms)   


def get_symmetry_generators(G: Graph, adjacency_dict: dict) -> np.ndarray:
    """
    Compute the number of automorphisms of a graph G, using pynauty.
    
    Args:
        G (Graph): Input graph (created with the Problems class).
        adjacency_dict (dict): Adjacency dictionary of G.
    
    Returns:
        ndarray: The matrix with a row for each generator.
    """
    N = G.get_number_of_nodes()
    g = Graph(N, directed=False, adjacency_dict=adjacency_dict)
    generators = autgrp(g)[0]
    
    return generators 


def get_symmetry_orbits(G: Graph, adjacency_dict: dict) -> Tuple[int, List]:
    """
    Compute the number of automorphisms of a graph G, using pynauty.
    
    Args:
        G (Graph): Input graph (created with the Problems class).
        adjacency_dict (dict): Adjacency dictionary of G.
    
    Returns:
        tuple: (number of orbits, orbits).
    """
    N = G.get_number_of_nodes()
    g = Graph(N, directed=False, adjacency_dict=adjacency_dict)
    num_orbits, orbits = autgrp(g)[4], autgrp(g)[3]
    
    return num_orbits, orbits