import tracemalloc
import gc


class A():
    pass

    def __del__(self):
        print('Dangerous!')


def funcext():
    a = A()
    b = A()
    a.chifan = b
    b.chifan = A

    del a
    del b

    print('垃圾回收哦', gc.collect())


if __name__ == '__main__':

    tracemalloc.start(25)  # 默认25个片段，这个本质还是多次采样
    funcext()  # 这是我自己定义的对象成员函数
    # 记录所有跟踪内存块的当前大小和峰值大小
    size, peak = tracemalloc.get_traced_memory()
    # 一个输出到控制台中，一个输出到文件
    print('memory blocks:{:>10.4f} KiB'.format(peak / 1024))
