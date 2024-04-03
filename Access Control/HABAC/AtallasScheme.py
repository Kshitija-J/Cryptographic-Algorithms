import networkx as nx
import hashlib


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


def generate_keys():
    """ Generate a unique key for a node. """
    return hashlib.sha256("unique_secret".encode()).hexdigest()

def derive_key(parent_key, child_label):
    """ Derive a child's key from the parent's key and child's label. """
    return hashlib.sha256((parent_key + child_label).encode()).hexdigest()


G = nx.DiGraph()

for role, sub_groups in senior_management.items():
    key = generate_keys()
    G.add_node(role, sub_groups=sub_groups, key=key, label=f"label_{role}")

for parent, children in senior_management.items():
    parent_key = G.nodes[parent]['key']
    for child in children:
        child_key = derive_key(parent_key, f"label_{child}")
        G.add_node(child, derived_key=child_key, label=f"label_{child}")
        G.add_edge(parent, child)   

G.add_node("CEO", key=generate_keys(), label="label_CEO")
G.add_edge("CEO", "CMO")
G.add_edge("CEO", "CIO")
G.add_edge("CEO", "CFO")

print("Graph Structure with Atallah's Scheme:")
for node in G.nodes:
    sub_groups = G.nodes[node].get("sub_groups", [])
    node_attributes = attributes.get(node, {})
    node_key = G.nodes[node].get("key", "No key assigned")
    derived_key = G.nodes[node].get("derived_key", "No derived key")
    print(f"Node: {node}, Sub-groups: {sub_groups}, Attributes: {node_attributes}, Key: {node_key}, Derived Key: {derived_key}")
