"""
序列化 (Serialization)
将对象的状态信息转换为便于存储或传输的形式的过程称之为序列化, 该过程的逆向则称之为反序列化, 如:
(1)数据和文本的转换
(2)Python的数据类型和二进制数据类型的转化
(3)Python的数据类型和json的转化

本文介绍使用json和pickle进行序列化和反序列化, 它们都提供了四种方法:
    dump() 把数据序列化并保存至文件
    dumps() 把数据序列化
    load() 从文件中读取数据并反序列化
    dumps() 把数据反序列化
"""

import json
import pickle

data = {
    'int': 1,
    'str': 'string',
    'list': [1, 2, 3],
}

"""json"""

# dumps()用法
# 把python数据转为json
json_data = json.dumps(data)
print('type:', type(json_data))
print('data:', json_data)

# loads()用法
# 再把json转为python数据
py_data = json.loads(json_data)
print('type:', type(py_data))
print('data:', py_data)

# dump()用法
# 把python数据存为.json文件
with open('py_to_json.json', 'w') as file:
    json.dump(data, file)

# load()用法
# 从.json文件中读取数据并转为python类型
with open('py_to_json.json', 'r') as file:
    py_data = json.load(file)
    print('type:', type(py_data))
    print('data:', py_data)

"""pickle"""
print('='*80)

# dumps()用法
# 把python数据转为byte类型
byte_data = pickle.dumps(data)
print('type:', type(byte_data))
print('data:', byte_data)

# loads()用法
# 再把byte类型转为python数据
py_data = pickle.loads(byte_data)
print('type:', type(py_data))
print('data:', py_data)

# dump()用法
# 把python数据存为.pkl
with open('py_to_byte.pkl', 'wb') as file:
    pickle.dump(data, file)

# load()用法
# 从.pkl文件中读取数据并转为python类型
with open('py_to_byte.pkl', 'rb') as file:
    py_data = pickle.load(file)
    print('type:', type(py_data))
    print('data:', py_data)
