import random
import time


class MyBigFatObject(object):
    pass


def computate_something(_cache={}):
    # 很明细的产生的泄漏的地址
    _cache[42] = dict(foo=MyBigFatObject(),
                      bar=MyBigFatObject())

    x = MyBigFatObject()  # 不会产生内泄漏
    sdfd333 = MyBigFatObject()  # 不会产生内泄漏


def main():
    # 在调用函数之前，我们对所有活着的对象进行快照
    print("-"*100)
    # 开始调用函数
    print("开始调用函数")
    computate_something()
    # 再执行一次快照建立
    print("-"*100)
    print("结束调用函数")


def do_more():
    for i in range(100):
        main()
        time.sleep(5)


if __name__ == "__main__":
    # main()
    do_more()


#  py-spy record -o profile.svg -- python /workspaces/memoryleaks/tools/test/t1.py
#  py-spy top -- python /workspaces/memoryleaks/tools/test/t1.py
