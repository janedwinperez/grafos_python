import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.graph["Name"] = "My Graph"

G.add_node('A', Age=19, Gender="F")
G.add_node('B', Age=18, Gender="M")
G.add_node('C', Age=22, Gender="M")
G.add_node('D', Age=21, Gender="M")
G.add_node('E', Age=20, Gender="F")

G.add_edge('A', 'C', weight=1)
G.add_edge('B', 'C', weight=0.5)
G.add_edge('B', 'D', weight=0.6)
G.add_edge('C', 'D', weight=0.8)
G.add_edge('D', 'E', weight=1)

pos = {
    "A" : (1,5),
    "B" : (4.5, 6.6),
    "C" : (3.6, 1.4),
    "D" : (5.8, 3.5),
    "E" : (7.9, 3.6)
    }

pos_node_attributes = {
    "A" : (-0.2, 5),
    "B" : (4.5, 7.5),
    "C" : (2.4, 1.4),
    "D" : (5.8, 2.5),
    "E" : (9.1, 3.6)
    }

for n,d in G.nodes(data=True):
    print(n)
    print(d)
    print("========================================")

node_labels = {n:(d['Age'], d['Gender']) for n,d in G.nodes(data=True)}

for u,v,d in G.edges(data=True):
    print(u,v)
    print(d)
    print("========================================")

edge_labels = {(u,v):d["weight"] for u,v,d in G.edges(data=True)}    
    
nx.draw(G, pos=pos, with_labels=True, node_color="red", node_size=3000,
        font_color="white", font_size=20,
        width=5)
nx.draw_networkx_labels(G, pos=pos_node_attributes, labels=node_labels,
                        font_color="black", font_size=12)
nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, label_pos=0.5)
plt.margins(0.2)
plt.show()
