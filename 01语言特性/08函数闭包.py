"""
    闭包: 在函数中嵌套了一个函数, 内部函数引用了外部函数中的变量, 并且外部函数的返回值是内部函数, 那么返回的内部函数被称为闭包,
简而言之, 闭包指延申作用域的函数.
    闭包的最大特点就是, 可以将父函数的变量和子函数绑定, 并返回绑定变量后的子函数, 此时即便父函数已经释放, 绑定的变量也不会释放,
而是可以被子函数继续引用, 装饰器的实现就是基于函数闭包.
    使用闭包需要注意的是, 在子函数中对父函数中的变量修改或者赋值时, 需要使用 nonlocal 关键字, 不然只是创建了一个和父函数中的变量
同名的局部变量.
"""


def parent():
    n = 100

    def child(v):
        # 对父函数中的变量修改或者赋值时, 需要使用 nonlocal 关键字
        nonlocal n
        n = n + v
        return n

    return child


print(parent()(10))
print(parent()(11))

# 可以围绕闭包的性质 实现 特定前缀+自增数字 的唯一码格式的算法
p = parent()
print(p(10))  # 110
print(p(10))  # 120
print(p(10))  # 130
