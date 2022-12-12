import objgraph
import os

x = ['a', '1', [2, 3]]
filename = os.path.dirname(__file__) + '/objgraph_test.png'
objgraph.show_refs([x], filename=filename)