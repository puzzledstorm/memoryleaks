# https://mg.pov.lt/objgraph/
# https://objgraph.readthedocs.io/en/stable/
# pip install xdot
# pip install objgraph
"""
https://stackoverflow.com/questions/59318212/image-renderer-dot-not-found-not-doing-anything-else

https://graphviz.gitlab.io/download/
sudo apt update
sudo apt install graphviz
"""

x = []
y = [x, [x], dict(x=x)]
import objgraph
# objgraph.show_refs([y], filename='sample-graph.png')

# objgraph.show_backrefs([x], filename='sample-backref-graph.png')
objgraph.show_most_common_types()


