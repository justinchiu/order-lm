# tree utils with a bert parser
from dataclasses import dataclass, field

@dataclass
class Node:
    index: int
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
    nodes = [Node(int(x)-1) for x in doc.values[0] if "-" not in x]
    # skip over multi-wordrange , the individual tokens should be included

    for i, h in enumerate(heads):
        if h > 0:
            nodes[h-1].children.append(i)

    return hi, nodes


def bfs(doc):
    L = len(doc.values[0])
    root, nodes = construct_graph(doc)
    queue = [nodes[root]]
    i = 0
    while i < L:
        node = queue[i]
        for child in node.children:
            queue.append(nodes[child])
        i += 1
    return [x.index for x in queue]

if __name__ == "__main__":
    from datasets import load_dataset
    import pdb

    ptb = load_dataset("ptb_text_only")

    import esupar
    nlp = esupar.load("en")

    data = ptb["train"]
    example = data[4]
    sentence = example["sentence"]#.replace(".", "").lower()
    doc = nlp(sentence)
    print(doc)
    import deplacy
    deplacy.render(doc)

    print(bfs(doc))
    pdb.set_trace()

