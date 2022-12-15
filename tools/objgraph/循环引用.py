import objgraph


class PAPA(object):
    pass


class MAMA(object):
    pass


# 创建两个对象
baba = PAPA()
mama = MAMA()
# 查看当前垃圾回收期的个数
print("PAPA的垃圾个数有", objgraph.count('PAPA'))
print("MAMA的垃圾个数有", objgraph.count('MAMA'))

# 引入循环引用的示例
baba.laopo = mama
mama.laogong = baba
print("=========================")
del baba
del mama
print("PAPA的垃圾个数有", objgraph.count('PAPA'))
print("MAMA的垃圾个数有", objgraph.count('MAMA'))


# https://www.modb.pro/db/144381