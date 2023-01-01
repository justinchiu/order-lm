from collections import defaultdict
from datasets import load_dataset, Dataset, DatasetDict

#import spacy
#from tree_utils import bfs

import esupar
from esupar_utils import bfs

ptb = load_dataset("ptb_text_only")
#nlp = spacy.load("en_core_web_sm")
nlp = esupar.load("en")

datadict = {}
for split, data in ptb.items():
    newdata = defaultdict(list)
    for i, example in enumerate(data):
        # remove periods because spacy has issues with it
        sentence = example["sentence"]
        doc = nlp(sentence)
        order = bfs(doc)

        newdata["sentence"].append(sentence)
        newdata["order"].append(order)

    datadict[split] = Dataset.from_dict(newdata)

newptb = DatasetDict(datadict)
newptb.save_to_disk("ptb_text_only_order")
import pdb; pdb.set_trace()
