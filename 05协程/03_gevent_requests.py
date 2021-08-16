import requests
import gevent
from gevent import monkey

monkey.patch_all()  # 一键替换多进程多线程关键字


def request_event():
    """请求事件"""
    print('begin')
    response = requests.get('http://httpbin.org/get')
    print(response.status_code)


def gevent_demo(n: int):
    """非阻塞式执行多个请求"""

    # 生成事件清单
    tasks = [gevent.spawn(request_event) for i in range(n)]
    # 把清单加入事件循环队列中
    gevent.joinall(tasks)


gevent_demo(5)
