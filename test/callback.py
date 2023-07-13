# 参考文档 https://blog.csdn.net/weixin_41605937/article/details/120248917
# https://zhuanlan.zhihu.com/p/363807663


def appy_async(func, args, *, callback):
    result = func(*args)
    callback(result)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


class ResultHandler(object):
    def __init__(self):
        self.sequence = 0

    def handle(self, result):
        self.sequence += 1
        print(f'{self.sequence} --- {result}')


def make_handler():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print(f'使用协程方式： {sequence} === {result}')


# 方式一：使用绑定的方式
ResultHandler = ResultHandler()
appy_async(add, (1, 10), callback=ResultHandler.handle)
appy_async(sub, (-29, 45), callback=ResultHandler.handle)

print("&&&&&")

# 方式二：使用协程的方式
handle = make_handler()
next(handle)
appy_async(add, (100, 675), callback=handle.send)
