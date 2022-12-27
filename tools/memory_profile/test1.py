import sys
import numpy as np


class MemLeak:
    def __init__(self, name):
        self.name = name
        self.huge_memory = np.random.random([1000, 1000, 10])
        self.child = None
        self.parent = None
    
    def __del__(self):
        print(f"对象 {self.name} 已经被删除。")
    
    def ref_count(self):
        print(f"对象 {self.name} 当前引用数为 {sys.getrefcount(self)}")


if __name__ == '__main__':
    fir = MemLeak('first normal')
    fir.ref_count()
    fir = []

    print("-"*150)
    fir = MemLeak('first loop')
    sec = MemLeak('second loop')
    fir.ref_count()
    sec.ref_count()

    # 循环引用
    #fir.child = sec
    import weakref
    fir.child = weakref.ref(sec)
    sec.parent = fir

    print("-"*150)
    fir.ref_count()
    sec.ref_count()

    print("-"*150)
    del sec
    fir.ref_count()
    del fir

    pass


# https://www.zywvvd.com/notes/coding/python/python-mem-leak/python-mem-leak/#%E5%BE%AA%E7%8E%AF%E5%BC%95%E7%94%A8
# htop 
# 循环引用这个倒是清楚了，但是实际上发生泄漏会是循环引用吗？