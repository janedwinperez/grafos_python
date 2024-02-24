import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()

G.add_nodes_from("ABCDE")
"""
G.add_node('A')
G.add_node('B')
G.add_node('C')
G.add_node('D')
G.add_node('E')
"""

G.add_edges_from(["AC", "BC", "BD", "CD", "DE"])
"""
G.add_edge('A', 'C')
G.add_edge('B', 'C')
G.add_edge('B', 'D')
G.add_edge('C', 'D')
G.add_edge('D', 'E')
"""

pos = {
    "A" : (1,5),
    "B" : (4.5, 6.6),
    "C" : (3.6, 1.4),
    "D" : (5.8, 3.5),
    "E" : (7.9, 3.6)
    }

nx.draw(G, pos=pos, with_labels=True, node_color="red", node_size=3000,
        font_color="white", font_size=20,
        width=5)
plt.margins(0.2)
plt.show()
