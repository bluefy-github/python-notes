"""
Python 基本数据结构
1. list (列表)
2. tuple (元组)
3. set (集合)
4. dict (字典)

容器(container):
    可以包含其他对象的对象被称为容器, 序列和映射是两种主要的容器类型
    序列(sequence):
        序列是一种数据结构, 这种结构的元素都有一个自动分配的数字类型的索引, 从0开始
        这种结构的容器: 列表 元组 字符串
    映射(mapping):
        映射是一种表达键值对的数据结构, 键可以是任何不可变的数据类型, 如数字, 字符串或元组, 但必须唯一
        这种结构的容器: 字典


(一) 列表和元组:
    元组可以看成一个不可变的列表
    相同点:
        1) 都是序列类型的容器对象, 可以支持任何类型的数据存放
        2) 都支持切片和迭代等操作
    不同点:
        1) 定义方式不同, 列表是[], 元组是(), 注意:定义一个元素的元组时, 一定要在元素后面加逗号
        2) 列表可变, 长度大小不固定, 可以进行增删改操作, 元组不可变, 长度大小固定, 不可以增删改
        3) 因为元组不可变, 所以可以作为字典的键, 列表不可以
        4) 储存相同元素时, 列表的大小比元组大
        5) 使用场景不同, 一般使用列表存储同类型数据, 用元组存储异构数据


(二) 集合
        集合是一种无序的, 无重复元素的序列类型的容器, 可以存储 int str float, bool, byte, tuple, frozenSet等不可变类型的元素
    frozenSet是冻结集合, 一旦定义不可增删改, 因为set可变不能用来表示子集, 所以用一般frozenSet来表示几集
        集合并不是严格意义上的序列对象, 集合可以迭代, 但不支持切片及索引

(三) 字典
        字典是一种键值对结构的映射类型的容器, 严格来说字典是无序的, 但是py3.6以后, 字典会根据定义时的顺序进行输出, 如果要确保字
    典的顺序可以使用collection模块中的OrderDict类型.


"""

"""1. 列表"""

# (1) 列表创建
# list2的创建方式效率比list1的高, 因为[]语法是由CPython直接解释执行的一个C函数,
# 而list()是由Python实现的一个方法, 调用该方法会涉及堆栈创建等一系列操作
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
