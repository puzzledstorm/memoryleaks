import time
from ctypes import CDLL
dgf = CDLL('./libdfunc.so')
# https://www.cnblogs.com/wuzaipei/p/11001925.html
# print(dgf.dgfunc(5))
# 动态编译 so文件 c语言
# gcc dfunc.c -fPIC -shared -o libdfunc.so
# 可执行文件编译
# gcc hello.o –o hello.exe
 
if __name__ == "__main__":
    st = time.time()
    for i in range(42):
        print("第{}次爬{}步".format(i,dgf.dgfunc(i)))
    print(time.time()-st)
