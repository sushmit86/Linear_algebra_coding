# Copyright Sushmit Roy
def dict2list(dct, keylist): return [dct[key] for key in keylist]

def list2dict(L, keylist): return {x:y for (x,y) in zip(keylist,L)}

def listrange2dict(L) : return {x:y for (x,y) in zip(range(len(L)),L)}