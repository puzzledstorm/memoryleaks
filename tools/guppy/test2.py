import sys
import guppy
import time
import logging
import os

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

# https://opensourcehacker.com/2008/03/07/debugging-django-memory-leak-with-trackrefs-and-guppy/
class TrackRefs:
    """Object to track reference counts across test runs."""

   # init heapy
    def __init__(self) -> None:
        self.heapy = guppy.hpy()

    # Print memory statistics
    def update(self):
        print(self.heapy.heap())

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
            computate_something()
            tracker.update() # Dump memory here
            time.sleep(10)
            break
           

def main():
    t = T()
    t.run()

main()
            
