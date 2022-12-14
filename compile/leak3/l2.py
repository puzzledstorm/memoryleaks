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
    # 第1步定位泄露的对象
    objgraph.show_growth()

    try:
        funcext()
    except:
        pass

    print("")
    objgraph.show_growth()
    # 第2：定位了哪个对象发生了内存泄露，那么接下来就是分析怎么泄露的，引用链是怎么样的
    objgraph.show_backrefs(objgraph.by_type(
        'A')[0], max_depth=10, filename='obj.png')
    # objgraph.show_refs([y], filename='sample-graph.png')
    objgraph.show_backrefs(objgraph.by_type(
        'A')[0], max_depth=20, filename='obj.png')
