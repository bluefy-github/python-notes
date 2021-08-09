"""
Python 基本数据结构
1. list (列表)
2. tuple (元组)
3. dict (字典)
4. set (集合)

list, tuple, set, dict都是可迭代对象, 都可以用for语句进行循环遍历, 都可以进行拆包
注意: 字典是键值对结构, 对字典进行遍历时, 遍历的是字典的键
(1) 列表和元组区别:
列表内的元素可以增删改, 元组内的元素不可以
列表不可以作为字典的键, 元组可以
一般使用列表类储存同类数据元素, 使用元组存储异构数据, 如:
# 定义元组
my_tup =  ('李四',  20)
# 定义列表
my_list = [('李四', 20), ('王五',  18)]

(2) 集合
集合可以存储 int str float, bool, byte, tuple类型的数据
注意: 不能存储set dict list 类型

"""

"""1. 列表"""

# (1) 列表创建
# list2的创建方式效率比list1的高, 因为[]语法是由CPython直接解释执行的一个C函数,
# 而list()是由Python实现的一个方法, 调用该方法会涉及堆栈创建的等一系列操作
list1 = list()
list2 = [1, 2, 3]

# (2) 给列表增加元素
list1.append(4)

# (3) 用一个列表拓展另一个列表
list1.extend(list2)
print(list1)  # [4, 1, 2, 3]

# (4) 列表浅拷贝问题
# list1增加元素5, list3中没有增加, 但是list2变化, list1和list3都有变化
# 原因是[1, 2, 3, list2]中存list2只是一个引用, 并不是list2对应的数据
list1.append(list2)
print('list1:', list1)
list3 = list1.copy()
print('list3:', list3)
list1.append(5)
list2.append(4)
print('list1:', list1)
print('list3:', list3)

# (5) 列表排序
# 排序以下列表 根据列表中的字典的键value的值正序排列
# 　排序除了
list4 = [
    {'index': 1, 'value': 8, },
    {'index': 2, 'value': 4, },
    {'index': 3, 'value': 6, },
]


def sort_func(item):

    """
    item指代列表中的元素 跟for关键字后的变量名等价
    函数中的语句较为简单时可以用 lambda 关键字 下面的语句跟本函数功能完全一致
    sort_func = lambda item: item['value'] # 左边函数名未给出的情况被称为匿名函数
    """
    return item['value']


print('list4无序:', list4)
list4.sort(key=sort_func)  # 正序
print('list4正序:', list4)
list4.sort(key=sort_func, reverse=True)  # 倒序
print('list4倒序:', list4)

"""2. 元组"""
_tup = (1, 2, 3)
_set = {1, 2, 3, 3}
_dict = {
    'k1': 'v1',
    'k2': 'v2',
    'k3': 'v3',
}
