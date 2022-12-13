from guppy import hpy
from pkgcore.config import load_config
c = load_config()
hp = hpy()

print(hp.heap())