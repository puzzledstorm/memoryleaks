import objgraph
import os
from ctypes import CDLL
import random


def leak():
    # leak = CDLL('./leak.so')
    leak = CDLL('/workspaces/memoryleaks/compile/leak/leak.so')
    n = 2
    if hasattr(leak, "leak"):
        leak.leak(n)
        # print(f"leak memory {n}M")

objgraph.show_growth(limit=3) 
leak()
print('-'*100)
objgraph.show_growth() 

filename = os.path.dirname(__file__) + '/chain.png'

objgraph.show_chain(
    objgraph.find_backref_chain(
        random.choice(objgraph.by_type('function')),
        objgraph.is_proper_module),
    filename=filename)

# roots = objgraph.get_leaking_objects()
# print(len(roots))
# filename = os.path.dirname(__file__) + '/test_leak.png'
# objgraph.show_refs(roots[:3], refcounts=True, filename=filename)
