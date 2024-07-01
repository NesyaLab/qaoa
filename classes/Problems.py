#------------------------------------------------------------------------------
# Problems.py
#
# This module defines a class `Problems` that facilitates the creation and manipulation
# of various types of graphs, intended for use with QAOA-type algorithms. The class 
# supports initialization with different graph types, including complete 
# graphs, star graphs, cycle graphs, barbell graphs, balanced trees, full r-ary trees, 
# 2D grids, Erdös-Renyi graphs, random d-regular graphs, and custom graphs from 
# adjacency matrices.
#
# The `Problems` class provides methods to:
# - Initialize with different graph types or a custom graph
# - Draw the graph using Matplotlib
# - Retrieve the graph object, nodes, edges, number of nodes, number of edges
# - Get the adjacency matrix, adjacency spectrum, Laplacian matrix, Laplacian spectrum
# - Get the adjacency dictionary of the graph
#
# A global variable `toy_graph` is defined for initialization purposes, representing 
# a default toy graph with 5 nodes.
#
# © Leonardo Lavagna 2024
# @ NESYA https://github.com/NesyaLab
#------------------------------------------------------------------------------


import numpy as np
import networkx as nx
from networkx import Graph
import matplotlib.pyplot as plt
from typing import List, Tuple


# GLOBAL VARIABLE
# Needed for initialization purposes: define a default toy graph with 5 nodes
toy_graph = nx.Graph()
toy_graph.add_edges_from([[0,3],[0,4],[1,3],[1,4],[2,3],[2,4]])


class Problems:
    def __init__(self, p_type: str = "toy_graph", G: Graph = toy_graph, verbose: bool = False):
        """Initialize class Problems.

        Args: 
            p_type (str): Problem type. The default is p_type="toy_graph" which has 5 nodes and 5 edges. Other types available: 
                              - complete graphs
                              - star graphs
                              - cycle graphs
                              - barbell graphs
                              - balanced trees
                              - full r-ary trees
                              - 2D grids
                              - Erdös-Renyi graphs
                              - Rando d-regular graphs
                          If an adjacency matrix is available, it's possible to build a graph with it using the type  
                          "from_adj_matrix". If a custom graph G is to be used, change p_type to None and p_type to "custom".
            G (Graph): A networkx graph that can be assigned by the user. The default is "toy_graph".
            verbose (bool): If True enters in debugging mode. The default is False.
        """
        self.verbose = verbose
        self.p_type = p_type
        self.G = G
        response = "N"
        if self.verbose is True:
            print(" --------------------------- ")
            print("| Intializing Problems class... |".upper())
            print(" --------------------------- ") 
            print("-> You are currently working with a pre-defined problem".upper())
            print("\t * Problem type: p_type = ", p_type)
            print("-> If you want to change it you can use:".upper())
            print("\t * complete_graph(<params>) where params = <num_nodes>")
            print("\t * star_graph(<params>) where params = <num_nodes>")
            print("\t * cycle_graph(<params>) where params = <num_nodes>")
            print("\t * barbell_graph(<params[0], params[1]>) where params = [<size_barbells>, <connecting_path_length>]")
            print("\t * balanced_tree(<params[0], params[1]>) where params = [<brancing_factor>, <height>]")
            print("\t * full_rary_tree(<params[0], params[1]>) where params = [<brancing_factor>, <num_nodes>]")
            print("\t * grid_2d_graph(<params[0], params[1]>) where params = [<x_nodes_coords>, <y_nodes_coords>]")
            print("\t * erdos_renyi_graph(<params[0], params[1]>) where params = [<num_nodes>, <edge_probability>]")
            print("\t * random_regular_graph(<params[0], params[1]>) where params = [<nodes_degree>, <num_nodes>]")
            print("\t * from_adj_matrix(<params>) where params =  numpy matrix (adjacency matrix)")
            print("\t * custom graphs by setting p_type='custom' and G=None.")
            print("-> Do you whish to change problem ? Answer Y or N to continue...".upper())
        if self.verbose is True:
            response = input()
        if response not in ["Y","N"]:
            raise Exception("Incompatible answer.")
        if response == "Y":
            self.p_type = input("Enter a problem type: ")
            if self.p_type == "complete_graph":
                self.params = input("Enter parameter: ")
                self.G = nx.complete_graph(int(self.params))
            if self.p_type == "star_graph":
                self.params = input("Enter parameter: ")
                self.G = nx.star_graph(int(self.params))
            if self.p_type == "cycle_graph":
                self.params = input("Enter parameter: ")
                self.G = nx.cycle_graph(int(self.params))
            if self.p_type == "barbell_graph":
                self.params = [input("Enter first parameter: "),input("Enter second parameter: ")]
                self.G = nx.barbell_graph(int(self.params[0]),int(self.params[1]))
            if self.p_type == "balanced_tree":
                self.params = [input("Enter first parameter: "),input("Enter second parameter: ")]
                self.G = nx.balanced_tree(int(self.params[0]),int(self.params[1]))
            if self.p_type == "full_rary_tree":
                self.params = [input("Enter first parameter: "),input("Enter second parameter: ")]
                self.G = nx.full_rary_tree(int(self.params[0]),int(self.params[1])) 
            if self.p_type == "grid_2d_graph":
                self.params = [input("Enter first parameter: "),input("Enter second parameter: ")]
                self.G = nx.grid_2d_graph(int(self.params[0]),int(self.params[1])) 
            if self.p_type == "erdos_renyi_graph":
                self.params = [input("Enter first parameter: "),input("Enter second parameter: ")]
                self.G = nx.erdos_renyi_graph(int(self.params[0]),float(self.params[1])) 
            if self.p_type == "random_regular_graph":
                self.params = [input("Enter first parameter: "),input("Enter second parameter: ")]
                self.G = nx.random_regular_graph(int(self.params[0]),int(self.params[1])) 
            if self.p_type == "from_adj_matrix":
                n = int(input("Enter the number of rows of the adjacency matrix:"))
                m = int(input("Enter the number of columns of the adjacency matrix:"))
                w = []
                print("Enter the all the elements row-wise:")
                for i in range(n):
                    a =[]
                    for j in range(m):
                        a.append(int(input()))
                    w.append(a)
                self.params = np.array(w)
                self.G = nx.from_numpy_array(np.array(w))
            
    
    def get_draw(self):
        """Get the draw of a graph created with the Problems' class.

        Note: The default toy graph is plotted with a bipartite layout, while other plots are displayed with default
        networkx's library parameters.
        """
        if self.p_type=="toy_graph":
            nx.draw_networkx(self.G, pos=nx.bipartite_layout(self.G, [0,1,2]))
        else:
            nx.draw_networkx(self.G)
            
    
    def get_graph(self):
        """Return the graph as a networkx object.

        Returns:
            Graph: the graph created with the Problems' class.
        """
        return self.G

    
    def get_nodes(self):
        """Get the nodes of a graph created with the Problems' class.

        Returns:
            List[int]: of nodes in the graph.
        """
        return self.G.nodes()

    
    def get_edges(self):
        """Get the edges of a graph created with the Problems' class.

        Returns:
            List[tuples[int,int]]: list of edge tuples representing the edges of the graph.
        """
        return self.G.edges()
    
    
    def get_number_of_nodes(self):
        """Get the number of nodes of a graph created with the Problems' class.

        Returns:
            int: The number of nodes in the graph.
        """
        return self.G.number_of_nodes()
    

    def get_number_of_edges(self):
        """Get the number of edges of a graph created with the Problems' class.

        Returns:
            int: The number of edges in the graph.
        """
        return self.G.number_of_edges()
    
    
    def get_adjacency_matrix(self):
        """Get the adjacency matrix of a graph created with the Problems' class.

        Returns:
            numpy.ndarray: the adjacency matrix of the graph.
        """
        return nx.to_numpy_array(self.G)


    def get_adjacency_spectrum(self):
        """Get the adjacency matrix spectrum of a graph created with the Problems' class.

        Returns:
            list: the spectrum of the adjacency matrix of the graph.
        """
        return nx.adjacency_spectrum(self.G)
    
    
    def get_laplacian(self):
        """Get the laplacian matrix of a graph created with the Problems' class.

        Returns:
            numpy.ndarray: the laplacian of the graph.
        """
        return nx.laplacian_matrix(self.G).toarray()


    def get_laplacian_spectrum(self):
        """Get the laplacian matrix spectrum of a graph created with the Problems' class.

        Returns:
            list: the spectrum of the laplacian of the graph.
        """
        return nx.laplacian_spectrum(self.G)
    
    
    def get_adjacency_dict(self):
        """Get the adjacency dictionary of a graph created with the Problems' class.

        Returns:
            dict: the adjacency dictionary of the graph.
        """
        dict_ = {}
        keys = self.get_nodes()
        values = []
        for key in keys:
            values.append([])
        for u,v in self.get_edges():
            for node in self.get_nodes():
                if u == node:
                    values[node].append(v)
                if v == node:
                    values[node].append(u)
        for i in keys:
            dict_[i] = values[i]
        
        return dict(sorted(dict_.items()))