"""
**参考链接:**
[1]  [Python Async/Await入门指南](https://zhuanlan.zhihu.com/p/27258289)
"""

import requests


# 请求事件 模拟网络IO环境
async def io_event():
    print('begin')
    requests.get('http://httpbin.org/get')
    print('end')
    return 200


# 错误调用:
# io_event()
# 正确调用:
# c = io_event()
# c.send(None)


# 写一个run()来运行协程
def run(coroutine):
    try:
        coroutine.send(None)  # 协程/生成器对象正常退出时 会抛出 StopIteration 异常
    except StopIteration as e:
        return e.value


print('=' * 50)
run(io_event())


# 在协程函数中，可以通过await语法来挂起自身的协程，并等待另一个协程完成直到返回结果
async def wait_io_event():
    print('wait begin')
    code = await io_event()
    print('wait end')
    return code


print('=' * 50)
run(wait_io_event())

"""事件循环"""


# 定义一个异步生成器
async def async_iterable(num):
    for i in range(num):
        yield io_event()


# async for关键字必须在异步方法内
async def event_loop():
    # async for语法表示我们要后面迭代的是一个异步生成器
    async for event in async_iterable(5):
        print(run(event))

print('=' * 50)
run(event_loop())
