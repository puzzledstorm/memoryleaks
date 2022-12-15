import random
import tracemalloc  # from 3.4

tracemalloc.start()  # 开始跟踪内存分配


class A():
    def __init__(self):
        super().__init__()

    def randomlist(self, n):
        lists = []
        l = [random.random() for i in range(n)]
        l.sort()
        for v in l:
            lists.append(v)
        return lists

    def randomlist2(self, n):
        lists = []
        l = [random.random() for i in range(n)]
        l.sort()
        for v in l:
            lists.append(v)
        return lists


A().randomlist(20)

snapshot1 = tracemalloc.take_snapshot()  # 快照，当前内存分配

A().randomlist(20000)

snapshot2 = tracemalloc.take_snapshot()  # 快照，当前内存分配


# 对比两个内存的快照
top_stats = snapshot2.compare_to(snapshot1, 'lineno')

# top_stats = snapshot.statistics('lineno')  # 快照对象的统计

for stat in top_stats[:10]:
    print(stat)