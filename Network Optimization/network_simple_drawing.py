# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 11:15:45 2018

@author: USER
"""
# %% 
import networkx as nx
from string import ascii_lowercase
# draw an empty graph
Graph_var = nx.Graph()
# add edges
Graph_var.add_edge(1,2,color='m',weight=6)
Graph_var.add_edge(2,3,color='black',weight=2)
Graph_var.add_edge(3,4,color='yellow',weight=4)

# color & display stuffs
position_1 = nx.circular_layout(Graph_var)
edges = Graph_var.edges()
colors = [Graph_var[u][v]['color'] for u,v in edges]
weights = [Graph_var[u][v]['weight'] for u,v in edges]
labels = {}
for idx, node in enumerate(Graph_var.nodes()): # label each nodes
    labels[node] = ascii_lowercase[idx]

# draw the network
nx.draw(Graph_var, position_1, edges=edges, edge_color=colors, width=weights,
        labels=labels)

# %% 
import networkx as nx
G=nx.dodecahedral_graph()
nx.draw(G)
nx.draw(G,pos=nx.spring_layout(G)) # use spring layout
import pylab
limits=pylab.axis('off') # turn of axis

