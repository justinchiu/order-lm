# tree utils
 
def find_root(doc):
    # finds the first root...
    # spacy is messed up, there can be multiple roots.
    for token in doc:
        if token.dep_ == "ROOT":
            return token
    return None

def inorder(root):
    return [root] + [x for c in root.children for x in inorder(c)]

def bfs(root):
    L = len(root.doc)
    queue = [root]
    i = 0
    while i < L:
        node = queue[i]
        for child in node.children:
            queue.append(child)
        i += 1
    return queue

if __name__ == "__main__":
    import spacy
    from datasets import load_dataset

    import streamlit as st
    import spacy_streamlit
    from spacy_streamlit import visualize_parser

    import pdb


    ptb = load_dataset("ptb_text_only")

    nlp = spacy.load("en_core_web_sm")

    for i, example in enumerate(ptb["train"]):
        sentence = example["sentence"].replace(".", "")
        doc = nlp(sentence)
        root = find_root(doc)
        #ordering = inorder(root)
        ordering = bfs(root)
        order = [x.i for x in ordering]
        oh_order = onehot(order)
        rel_emb(order)
        if i > 0:
            st.write(root.text, root.i, root.dep_, list(root.children))
            st.write(ordering)
            visualize_parser(doc, displacy_options={"compact":True})
            pdb.set_trace()


