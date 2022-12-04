import tracemalloc
import sys
from example_1 import Process
import numpy as np


class Analysis_Memory:
    def __init__(self):
        tracemalloc.start()
        print("__init__")


    def start(self):
        current, peak = tracemalloc.get_traced_memory()
        self.start = current
        self.last = current

    def increase(self, name, *args):
        current, peak = tracemalloc.get_traced_memory()
        usage = round((current - self.last) / 10**6)
        excepted = sum([sys.getsizeof(arg) for arg in args])
        excepted = round(excepted / 10**6)
        print(f"{name:<15} : memory usage chanegd is {usage} MB; except is {excepted} MB")
        self.last = current

    def delete_1(self, *args):
        excepted = sum([sys.getsizeof(arg) for arg in args])
        excepted = round(excepted / 10**6)
        self.excepted = -excepted

    def delete_2(self, name):
        current, peak = tracemalloc.get_traced_memory()
        usage = round((current - self.last) / 10**6)
        excepted = self.excepted
        print(f"{name:<15} : memory usage chanegd is {usage} MB; except is {excepted} MB")
        self.last = current
        self.excepted = None



    def __del__(self):
        print("__del__")
        tracemalloc.stop()


# 分析每个部分增加了多少内存
analysis = Analysis_Memory()
m = Process()

analysis.start()
for i in range(100):
    frame = np.zeros((8000,8000))
    analysis.increase("imread", frame)
    # ===========================================

    encoded = m.encode(frame)
    analysis.increase("encode", encoded)
    # ===========================================

    analysis.delete_1(frame)
    del frame
    analysis.delete_2("del frame")
    # ===========================================

    frame = m.decoce(encoded)
    analysis.increase("decoce", frame)
    # ===========================================

    analysis.delete_1(encoded)
    del encoded
    analysis.delete_2("del encoded")
    # ===========================================

    frame2 = m.crop(frame)
    analysis.increase("crop", frame2)
    # ===========================================

    analysis.delete_1(frame)
    del frame
    analysis.delete_2("del frame")
    # ===========================================

    analysis.delete_1(frame2)
    del frame2
    analysis.delete_2("del frame2")
    # ===========================================

    break