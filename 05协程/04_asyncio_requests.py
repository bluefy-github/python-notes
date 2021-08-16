import requests
import asyncio


async def io_event():
    print('begin')
    return requests.get('http://httpbin.org/get')


def io_event_callback(instance):
    response = instance.result()
    print(response.json())


def single_run():
    """单任务"""
    # 创建 future 对象
    future = asyncio.ensure_future(io_event())
    # 为 future 定义回调函数
    future.add_done_callback(io_event_callback)
    # 获取事件循环对象
    loop = asyncio.get_event_loop()
    # 把 future 注册到事件循环中
    loop.run_until_complete(future)


def multi_run(n: int):
    """多任务"""

    futures = []
    for i in range(n):
        # 创建 future 对象
        future = asyncio.ensure_future(io_event())
        # 为 future 定义回调函数
        future.add_done_callback(io_event_callback)
        futures.append(future)

    tasks = asyncio.wait(futures)
    # 获取事件循环对象
    loop = asyncio.get_event_loop()
    # 把 future 注册到事件循环中
    loop.run_until_complete(tasks)


single_run()
print('=' * 50)
multi_run(5)
