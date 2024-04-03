import networkx as nx

G = nx.DiGraph()


senior_management = {
    "CMO": ["Head of Surgery", "Head of Internal Medicine", "Head of Pediatrics", "Head of Nursing"],
    "CIO": ["IT Department Head"],
    "CFO": ["HR Department Head", "Finance Department Head"]
}


for role, sub_groups in senior_management.items():
    G.add_node(role, sub_groups=sub_groups)

G.add_edge("CEO", "CMO")
G.add_edge("CEO", "CIO")
G.add_edge("CEO", "CFO")


print("Sub-groups of CMO:", G.nodes["CMO"]["sub_groups"])

for node in G.nodes:
    sub_groups = G.nodes[node].get("sub_groups", [])
    print(f"Node: {node}, Sub-groups: {sub_groups}")
