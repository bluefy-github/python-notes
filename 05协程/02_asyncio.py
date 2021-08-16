import asyncio
import requests


async def await_demo(n):
    print(f'begin---{n}')
    await asyncio.sleep(1)
    print(f'end---{n}')


async def request_event():
    print('begin')
    response = requests.get('http://httpbin.org/get')
    print('end', response.status_code)


def run(tasks: list):
    loop = asyncio.get_event_loop()
    tasks = asyncio.wait(tasks)
    loop.run_until_complete(tasks)
    loop.close()


# await_demo_tasks = [await_demo(i) for i in range(5)]
# run(await_demo_tasks)

request_event_tasks = [request_event() for i in range(5)]
run(request_event_tasks)  # 这种方式还是同步运行
