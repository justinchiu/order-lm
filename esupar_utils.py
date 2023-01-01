# tree utils with a bert parser
from dataclasses import dataclass, field

@dataclass
class Node:
    id: str
    token: str
    head: str 
    children: list[int] = field(default_factory=list)


def find_root(doc):
    # finds the first root...
    heads = doc.values[6]
    rels = doc.values[7]
    assert hi == ri
    return hi

def construct_graph(doc):
    heads = doc.values[6]
    rels = doc.values[7]

    hi = heads.index(0)
    ri = rels.index("root")

    # adjacency list
    #nodes = [Node(int(x)-1) for x in doc.values[0] if "-" not in x]
    nodes = {}
    node2idx = {}
    idx2node = []
    for id, tok, head in zip(doc.values[0], doc.values[1], heads):
        # skip over multi-wordrange , the individual tokens should be included
        if "-" not in id and tok != "_":
            node = Node(id, tok, str(head))
            nodes[id] = node
            node2idx[id] = len(idx2node)
            idx2node.append(id)

    # fill in children
    for node in nodes.values():
        if node.head != "0":
            nodes[node.head].children.append(node.id)

    return nodes[doc.values[0][hi]], nodes, node2idx, idx2node


def bfs(doc):
    root, nodes, node2idx, idx2node = construct_graph(doc)
    L = len(idx2node)
    queue = [root]
    i = 0
    while i < L:
        node = queue[i]
        for child in node.children:
            queue.append(nodes[child])
        i += 1
    return [node2idx[x.id] for x in queue]

if __name__ == "__main__":
    from datasets import load_dataset
    import pdb

    ptb = load_dataset("ptb_text_only")

    import esupar
    nlp = esupar.load("en")

    data = ptb["train"]
    example = data[1716]
    sentence = example["sentence"]
    doc = nlp(sentence)
    print(doc)
    import deplacy
    deplacy.render(doc)

    print(bfs(doc))
    pdb.set_trace()

