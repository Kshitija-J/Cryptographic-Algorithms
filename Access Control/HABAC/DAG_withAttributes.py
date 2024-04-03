import networkx as nx

G = nx.DiGraph()

senior_management = {
    "CMO": ["Head of Surgery", "Head of Internal Medicine", "Head of Pediatrics", "Head of Nursing"],
    "CIO": ["IT Department Head"],
    "CFO": ["HR Department Head", "Finance Department Head"]
}

attributes = {
    "CMO": {"specialization": "Medical", "access_level": "High"},
    "CIO": {"specialization": "Information Technology", "access_level": "High"},
    "CFO": {"specialization": "Finance", "access_level": "High"},
}

for role, sub_groups in senior_management.items():
    G.add_node(role, sub_groups=sub_groups)


G.add_edge("CEO", "CMO")
G.add_edge("CEO", "CIO")
G.add_edge("CEO", "CFO")

print("Graph Structure:")
for node in G.nodes:
    sub_groups = G.nodes[node].get("sub_groups", [])
    node_attributes = attributes.get(node, {})
    print(f"Node: {node}, Sub-groups: {sub_groups}, Attributes: {node_attributes}")

