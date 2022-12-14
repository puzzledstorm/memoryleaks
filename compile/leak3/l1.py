import objgraph

_cache = []


class A():
    pass


def funcext():
    a = A()
    _cache.append(a)

    if True:
        return

    _cache.remove(a)


if __name__ == '__main__':
    # 第一步定位泄露的对象
    objgraph.show_growth()

    try:
        funcext()
    except:
        pass

    print("调用函数后")
    objgraph.show_growth()
