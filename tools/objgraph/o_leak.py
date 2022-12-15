import random
import objgraph


class MyBigFatObject(object):
    pass


def computate_something(_cache={}):
    # 很明细的产生的泄漏的地址
    _cache[42] = dict(foo=MyBigFatObject(),
                      bar=MyBigFatObject())
  
    x = MyBigFatObject()  # 不会产生内泄漏
    sdfd333 = MyBigFatObject() # 不会产生内泄漏




# 在调用函数之前，我们对所有活着的对象进行快照
print("-"*100)
objgraph.show_growth(limit=3)
# 开始调用函数
computate_something()
# 再执行一次快照建立
print("-"*100)
objgraph.show_growth()

# https://www.modb.pro/db/144381