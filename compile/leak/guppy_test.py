import sys
import guppy
import time
import logging
import os
from ctypes import CDLL
import random
from pkgcore.config import load_config
from guppy import hpy


def leak():
    # leak = CDLL('./leak.so')
    leak = CDLL('/workspaces/memoryleaks/compile/leak/leak.so')
    n = 10
    if hasattr(leak, "leak"):
        leak.leak(n)
        print(f"leak memory {n}M")

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG,
                    filename='guppy.log',
                    filemode='a')
logger = logging.getLogger('test')


class MyBigFatObject(object):
    pass


def computate_something(_cache={}):
    _cache[42] = dict(foo=MyBigFatObject(),
                      bar=MyBigFatObject())
    # a very explicit and easy-to-find "leak" but oh well
    x = MyBigFatObject() # this one doesn't leak

# https://smira.ru/wp-content/uploads/2011/08/heapy.html
class TrackRefs:
    """Object to track reference counts across test runs."""

   # init heapy
    def __init__(self) -> None:
        self.heapy = guppy.hpy()

    # Print memory statistics
    def update(self):
        h = self.heapy.heap()
        print(h)
        print("-"*100)
        print(h[0])
        print("-"*100)
        print(h.bytype)
        print("-"*100)
        print(h.byrcs)
        print("-"*100)
        print(h[0].byrcs[0].referrers.byrcs)


    # Print relative memory consumption since last sycle
    def update1(self):
        print(self.heapy.heap())
        self.heapy.setref()

    # Print relative memory consumption w/heap traversing
    def update2(self):
        print(self.heapy.heap().get_rp(40))
        self.heapy.setref()

class T:
    def __init__(self) -> None:
         self.running = False

    def run(self):
        self.running = True
        logger.info(f"Started worker {os.getpid()}")
        # Memory leak tracking
        tracker = TrackRefs()

        while self.running:
            # computate_something()

            # leak()
    
            c = load_config()
            tracker.update() # Dump memory here
            time.sleep(10)
            break
           

def main():
    t = T()
    t.run()

main()
            
