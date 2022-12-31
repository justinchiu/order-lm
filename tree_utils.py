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

def bfs(doc):
    root = find_root(doc)
    L = len(root.doc)
    queue = [root]
    i = 0
    while i < L:
        node = queue[i]
        for child in node.children:
            queue.append(child)
        i += 1
    return [x.i for x in queue]

if __name__ == "__main__":
    import spacy
    from datasets import load_dataset

    import streamlit as st
    import spacy_streamlit
    from spacy_streamlit import visualize_parser

    import pdb


    ptb = load_dataset("ptb_text_only")

    #nlp = spacy.load("en_core_web_sm")
    import esupar
    nlp = esupar.load("en")

    data = ptb["train"]
    example = data[4]

    sentence = example["sentence"].replace(".", "").lower()
    doc = nlp(sentence)
    import pdb; pdb.set_trace()
    root = find_root(doc)
    #ordering = bfs(root)
    st.write(sentence)
    st.write(root.text, root.i, root.dep_, list(root.children))
    #st.write(ordering)
    visualize_parser(doc, displacy_options={"compact":True})

