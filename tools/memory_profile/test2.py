import sys
import numpy as np


if __name__ == '__main__':

    # 建立对象
    test = {}
    # 默认对象引用数量为 2
    print(sys.getrefcount(test)) 		# 2 
    # 为该对象建立引用
    quo = test
    # 添加引用后，二者引用数量为 3
    print(sys.getrefcount(quo)) 		# 3 
    print(sys.getrefcount(test)) 		# 3 
    # 删除引用
    del quo
    # 删除引用后，引用数变回 2
    print(sys.getrefcount(test))		# 2
    # 重新添加相同的引用
    quo = test
    # 和之前一样，引用数变为 3
    print(sys.getrefcount(quo))			# 3
    print(sys.getrefcount(test))		# 3
    # 创建新对象(空列表) 覆盖原始 test 对象(空字典)
    test = []
    # quo 保持对空字典的引用，新对象仅有自己的引用，因此二者都为 2
    print(sys.getrefcount(quo))			# 2
    print(sys.getrefcount(test))		# 2
    print(test, quo)					# [] {}
    pass