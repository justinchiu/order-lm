# ordering utils
# see https://github.com/xuanlinli17/autoregressive_inference/blob/b2c8e01b6d72d2291bb4d8816b6cf4a04fa46741/voi/permutation_utils.py
 
import numpy as np

import pdb

def onehot(order):
    T = len(order)
    oh = np.zeros((T, T))
    oh[np.arange(T), order] = 1
    return oh

def rel_emb(order):
    # unsorted_relative
    T = len(order)

    lt = order < order[:,None]
    eq = order == order[:,None]
    gt = order > order[:,None]

    re = np.zeros((T,T))
    re[lt] = -1
    re[gt] = 1
    return re

def sorted_ptr(re):
    T = re.shape[-1]
    tr = np.triu(re)
    return (tr > 0).sum(-2)

def partial_pos(re):
    return np.tril(np.maximum(re, 0).cumsum(-2))

def insertion_index(re):
    # insert re[i] to the right of out[i]
    pp = partial_pos(re)
    return (np.tril(pp) * (re == -1)).max(1)

if __name__ == "__main__":
    order = np.array([0,3,2,1])
    re = rel_emb(order)
    assert (re == np.array([[0,1,1,1],[-1,0,-1,-1],[-1,1,0,-1],[-1,1,1,0]])).all()

    order = np.array([0,2,3,1,4])
    re = rel_emb(order)
    assert (re == np.array([[0,1,1,1,1],[-1,0,1,-1,1],[-1,-1,0,-1,1],[-1,1,1,0,1],[-1,-1,-1,-1,0]])).all()
    sptr = sorted_ptr(re)
    assert (sptr == np.array([0,1,2,1,4])).all()
    print(sptr)
    pp = partial_pos(re)
    assert (pp == np.array([[0,0,0,0,0],[0,1,0,0,0],[0,1,2,0,0],[0,2,3,1,0],[0,2,3,1,4]])).all()
    ii = insertion_index(re)
    assert (ii == np.array([0,0,1,0,3])).all()
