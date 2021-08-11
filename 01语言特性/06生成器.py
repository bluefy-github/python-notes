"""
包含yield关键的方法被称为生成器
"""


def generator_func():
    n = yield 1
    print(n)  # 在g.send(11)时 才会执行该语句
    n = yield 2
    print(n)
    n = yield 3
    print(n)


g = generator_func()
print(g.send(None))  # 1
print(g.send(11))  # 2

# 1
# 11
# 2
