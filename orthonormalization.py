# Copyright 2013 Philip N. Klein
# Changed By Sushmit Roy

from orthogonalization import *
from vec import  *
from mat import *
from matutil import *
from dictutil import dict2list, list2dict

def adjust(v, multipliers):
    for index,value in enumerate(v):
        multipliers[index] = value * multipliers[index]
    return multipliers


def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list T of orthonormal Vecs such that for all i in [1, len(L)],
            Span L[:i] == Span T[:i]

    >>> from vec import Vec
    >>> D = {'a','b','c','d'}
    >>> L = [Vec(D, {'a':4,'b':3,'c':1,'d':2}), Vec(D, {'a':8,'b':9,'c':-5,'d':-5}), Vec(D, {'a':10,'b':1,'c':-1,'d':5})]
    >>> for v in orthonormalize(L): print(v)
    ... 
    <BLANKLINE>
    b    a     c     d
    -----------------------
    0.548 0.73 0.183 0.365
    <BLANKLINE>
    b     a      c      d
    --------------------------
    0.403 0.187 -0.566 -0.695
    <BLANKLINE>
    b     a      c     d
    --------------------------
    -0.653 0.528 -0.512 0.181
    '''
    pass
    Lstar = orthogonalize(L)
    for index, item in enumerate(Lstar):
        norm = item * item # doing the dot product returns the norm
        if norm != 0 :
            Lstar[index] = (norm ** (-0.5))*item
    return Lstar





def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)

    >>> from vec import Vec
    >>> D={'a','b','c','d'}
    >>> L = [Vec(D, {'a':4,'b':3,'c':1,'d':2}), Vec(D, {'a':8,'b':9,'c':-5,'d':-5}), Vec(D, {'a':10,'b':1,'c':-1,'d':5})]
    >>> Qlist, Rlist = aug_orthonormalize(L)
    >>> from matutil import coldict2mat
    >>> print(coldict2mat(Qlist))
    <BLANKLINE>
    0      1      2
    ---------------------
    b  |  0.548  0.403 -0.653
    a  |   0.73  0.187  0.528
    c  |  0.183 -0.566 -0.512
    d  |  0.365 -0.695  0.181
    <BLANKLINE>
    >>> print(coldict2mat(Rlist))
    <BLANKLINE>
    0    1      2
    ------------------
    0  |  5.48 8.03   9.49
    1  |     0 11.4 -0.636
    2  |     0    0   6.04
    <BLANKLINE>
    >>> print(coldict2mat(Qlist)*coldict2mat(Rlist))
    <BLANKLINE>
    0  1  2
    ---------
    b  |  3  9  1
    a  |  4  8 10
    c  |  1 -5 -1
    d  |  2 -5  5
    '''
    pass
    Qlist = orthonormalize(L)
    Qlist_unormalized , Rlist = aug_orthogonalize(L)
    v = [(item*item)**(1/2) for item in Qlist_unormalized]
    multipliers = mat2rowdict(coldict2mat(Rlist))
    Rlist = mat2coldict(rowdict2mat(adjust(v, multipliers)))
    Rlist = dict2list(Rlist, range(len(Qlist)))
    return Qlist, Rlist


