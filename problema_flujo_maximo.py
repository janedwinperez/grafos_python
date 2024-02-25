import networkx as nx

G = nx.DiGraph()
G.add_nodes_from(["S", "A", "B", "C", "T"])

G.add_edges_from([
    ("S", "A", {"capacity" : 12}),
    ("S", "B", {"capacity" : 8}),
    ("S", "C", {"capacity" : 5}),
    ("A", "B", {"capacity" : 10}),
    ("A", "C", {"capacity" : 9}),
    ("B", "T", {"capacity" : 5}),
    ("C", "B", {"capacity" : 7}),
    ("C", "T", {"capacity" : 16})
    ])


from networkx.algorithms.flow import shortest_augmenting_path
flow_value, flow_dict =nx.maximum_flow(G, "S", "T", flow_func=shortest_augmenting_path)
print(flow_value)
print("==============================")
print(flow_dict)
