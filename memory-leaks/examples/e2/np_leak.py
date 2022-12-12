import numpy as np
from mem_top import mem_top
import logging

logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.DEBUG,
                    filename='test.log',
                    filemode='a')
logger = logging.getLogger('test')


def one():
    n = 2
    l = []
    for i in range(n):
        array_large = np.random.choice(1000, size=(7000, 7000))
        array_small = array_large[:5, :5]
        l.append(array_small)
    print(l)

def run():
    for x in range(10):
        print(x)
        one()
        # From time to time:
        logger.info(mem_top())
        print(mem_top())

if __name__ == "__main__":
    run()
    # one()