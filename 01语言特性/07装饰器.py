"""
    装饰器: 装饰器本质是一个嵌套函数, 它接收一个函数类型的参数, 这个参数称为为目标函数, 然后围绕目标函数实现各种操作来给目标函
数增加新的功能, 而装饰器之所以受欢迎是因为, 使用时非常简洁, 在函数上方添加@符号就可以对函数进行增强.
"""
import time


def run_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)  # 函数在这里运行
        end = time.time()
        cost_time = end - start
        print("run time {}".format(cost_time))

    return inner


# @run_time 等价于 demo_func = run_time(demo_func)
# 打印 demo_func 的函数名, 会发现函数名是 inner
# 此时 demo_func 是变量名, 指向函数 run_time 的返回值 inner 函数
# demo_func() 等价于 inner()
@run_time
def demo_func():
    time.sleep(1)


print('demo_func name is:', demo_func.__name__)
demo_func()


# 带参数的装饰
def grand(msg):
    def parent(func):
        def child(*args, **kwargs):
            start = time.time()
            func()  # 函数在这里运行
            end = time.time()
            cost_time = end - start
            print("run time {}".format(cost_time))
            print('msg:', msg)

        return child

    return parent


@grand(msg='12345678910')
def demo_func():
    time.sleep(1)


print('=' * 50)
print('demo_func name is:', demo_func.__name__)
demo_func()
