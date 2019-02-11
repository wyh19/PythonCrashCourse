# 函数就是带名字的代码块，用于完成具体的工作；如果一段代码会多次被执行，那么应该考虑将其定义为函数，然后调用函数执行该段代码

# 函数定义的形式为 
# def 函数名():
#   """函数说明（可选）"""
#   函数体（缩进）

def greet_user():
    """显示简单的问候语"""
    print('Hello')

# 函数调用
greet_user()

# 通过参数，想函数传递额外数据，使其具备更多功能
def greet_user2(username): 
    """显示姓名的问候语"""
    print("Hello, " + username.title() + "!")

# 函数调用，传入参数'jesse'，该参数赋值给函数形参username
# 根据学术划分，username是形参（函数定义时的参数），'jesse'是实参（实际传入的参数）；函数调用时，实参赋值给形参
greet_user2('jesse')
