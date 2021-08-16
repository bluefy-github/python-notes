"""
包含yield关键的方法被称为生成器
"""


def yield_demo():
    n = yield 1  # 给send()传的参数会赋值给yield左边的变量n
    print(n)
    n = yield 2
    print(n)
    n = yield 3
    print(n)
    return n


# 调用方式(1)
print('=' * 50)
g2 = yield_demo()
print(g2.send(None))  # 启动时参数必须为None
print(g2.send(11))

# 调用方式(2)
print('=' * 50)
for item in yield_demo():
    print(item)

# 调用方式(3)
# 注意:第四次执行时 会抛出 StopIteration 异常
print('=' * 50)
g = yield_demo()
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3


# yield from 的用法
def yield_from_demo():
    print('yield_from_demo is running...')
    n = yield from yield_demo()  # yield from 会把右边表达式的返回值赋给左边的变量
    print('n:', n)


print('=' * 50)
yf = yield_from_demo()

# 下面的send()实际是yield_demo().send()
yf.send(None)
yf.send('A')
yf.send('B')
yf.send('C')
