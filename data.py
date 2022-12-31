from collections import defaultdict
from datasets import load_dataset
import spacy

from tree_utils import find_root, bfs

ptb = load_dataset("ptb_text_only")
nlp = spacy.load("en_core_web_sm")

datadict = {}
for split, data in ptb.items():
    newdata = defaultdict(list)
    for i, example in enumerate(data):
        # remove periods because spacy has issues with it
        sentence = example["sentence"].replace(".", "").replace("<unk>", "unk").lower()
        doc = nlp(sentence)
        root = find_root(doc)
        ordered = bfs(root)
        order = [x.i for x in ordered]

        newdata["sentence"].append(sentence)
        newdata["order"].append(order)

    datadict[split] = Dataset.from_dict(newdata)
    import pdb; pdb.set_trace()
