"""

"""

import requests

"""普通函数"""


def func():
    return 1


# 调用方式:
print('func():', func())  # func(): 1

"""生成器函数"""


def generator_func():
    yield 1
    yield 2
    yield 3


# 错误调用:
print('generator_func():', generator_func())  # generator_func(): <generator object generator_func at xxx>
# 正确调用:
g = generator_func()
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3
# print(next(g))  # 第四次执行时 会抛出 StopIteration 异常


"""协程函数"""


async def coroutine_func():
    # 模拟耗时操作
    print('begin')
    response = requests.get('http://httpbin.org/get')  # 执行到这一步时 解释器不会等待完成 而是会去执行其他任务
    return response.status_code


# 错误调用:
# print('coroutine_func():', coroutine_func())  # coroutine_func(): <coroutine object coroutine_func at xxx>

# 正确调用
try:
    coroutine_func().send(None)  # 协程/生成器对象正常退出时 会抛出 StopIteration 异常
except StopIteration as e:
    print(e.value)


# 一般会写一个run()来运行协程
def run(coroutine):
    try:
        coroutine.send(None)
    except StopIteration as si:
        return si.value


# 在协程函数中，可以通过await语法来挂起自身的协程，并等待另一个协程完成直到返回结果
async def coroutine_func2():
    result = await coroutine_func()
    return result


print(run(coroutine_func2()))  # 200

"""事件循环"""


# 定义一个异步生成器
async def async_iterable(num):
    for i in range(num):
        yield coroutine_func()


# async for关键字必须在异步方法内
async def event_loop():
    # async for语法表示我们要后面迭代的是一个异步生成器
    print('=' * 50)
    async for event in async_iterable(10):
        print(run(event))


run(event_loop())
