"""
    可迭代对象可以使用for循环进行遍历, 如list, set, tuple, str等都是可迭代对象
    迭代器除了可以用for循环, 还可以使用next()进行遍历
"""

_list = [1, 2, 3, 4, 5]
_iter = iter(_list)  # 此时 _iter 是迭代器

# 使用next()遍历
print(next(_iter))
print(next(_iter))

# while 和 next() 结合
while True:
    try:
        print('while:', next(_iter))
    except StopIteration:
        break

''' output:
1
2
while: 3
while: 4
while: 5
'''

# next(_list)  # 可迭代对象, 不能对其使用 next()

''' output:
TypeError: 'list' object is not an iterator
'''

# len(_iter)  # 迭代器, 不能对其使用 len()

''' output:
TypeError: object of type 'list_iterator' has no len()
'''


# 自定义迭代对象
class MyIterable:
    """
    实现了__iter__()的类被称为可迭代对象
    """

    def __init__(self):
        self.result = ['a', 'b', 'c', 'd', 'e']

    def __getitem__(self, index):
        """
        对该类进行for循环时 如果__iter__()方法不存在 会调用该方法
        """

        print('__getitem__方法被调用...')
        return self.result[index]

    def __iter__(self):
        """
        对该类进行for循环时 会调用该方法 该方法的必须返回迭代器
        """

        print('__iter__方法被调用...')
        for item in self.result:
            yield item


_iterable = MyIterable()

# 使用next()方法
# 如果没有实现__iter__(), 使用iter()方法会报错
it = iter(_iterable)
print('it:', next(it))
print('it:', next(it))

''' output:
__iter__方法被调用...
it: a
it: b
'''

# 如果没有实现__iter__(), 但实现了__getitem__(), 也可以执行for循环
for each in _iterable:
    print(each)

''' output:
__iter__方法被调用...
a
b
c
d
e
'''


# 自定义迭代器
class MyIterator:
    """
    实现了 __iter__() 和 __next__() 的类被称为迭代器
    """

    def __init__(self):
        self.result = ['a', 'b', 'c', 'd', 'e']
        self.index = 0

    def __iter__(self):
        """
        对该类进行for循环时 会调用该方法 该方法的必须返回迭代器
        """

        print('__iter__方法被调用...')
        return self  # 返回自身, 因为其本身是一个迭代器

    def __next__(self):
        """
        对该类进行next()方法时 会调用该方法
        """

        print('__next__方法被调用...')
        if self.index > len(self.result) - 1:
            raise StopIteration  # 这个异常不会抛出, 而是会终止循环
        result = self.result[self.index]
        self.index += 1
        return result


_iterator = MyIterator()

# 使用next()方法
print(next(_iterator))
print(next(_iterator))
''' output:
__next__方法被调用...
a
__next__方法被调用...
b
'''

# 进行for循环
for each in _iterator:
    print(each)

''' output:
__iter__方法被调用...
__next__方法被调用...
c
__next__方法被调用...
d
__next__方法被调用...
e
__next__方法被调用...
'''
