"""
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

# 创建方式
_list = [1, 2, 3]
_tup = (1, 2, 3)
_set = {1, 2, 3, 3}
_dict = {
    'k1': 'v1',
    'k2': 'v2',
    'k3': 'v3',
}

_set2 = {_list}  # TypeError: unhashable type: 'list'

_set3 = {_tup}
print(_set3)

# _set4 = {_set}  # TypeError: unhashable type: 'set'
# print(_set4)

# _set5 = {_dict}  # TypeError: unhashable type: 'dict'
# print(_set4)
