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

# 当有函数有多个参数时，实参可以按形参的顺序依次传入，成为位置实参
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# 两个参数依次传入，分别对应各自所在位置的形参
print('\n---按顺序传参---')
describe_pet('hamster', 'harry')

# 思考：如果参数很多，顺序容易考错，如果我可以指定参数名传参就好了，这可以吗？
# 答案： 可以的，python支持关键字实参，即给指定名称的形参传入参数，看下面示例

# 给指定参数名传参，再也不用担心顺序问题了
print('\n---关键字传参---')
describe_pet(pet_name='harry', animal_type='hamster')

# 参数默认值，即在定义函数时，给某些参数指定默认值，在调用函数时，当不给这些含有默认值的参数传参时，它们使用各自的默认值作为参数
def describe_pet2(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# 可以灵活的混合使用默认参数、关键字传参
print('\n---使用默认值---')
describe_pet2('旺财')
describe_pet2(pet_name='旺财')
print('\n---覆盖默认值---')
describe_pet2('喵喵', 'cat')
describe_pet2('喵喵', animal_type='cat')


# 将实参变成可选，即将有默认值得参数放置在参数列表末尾
def print_name(first_name, last_name, middle_name=''):
    """按正常顺序，middle_name应该放在第二个，但是因为有些人没有middle_name,那么将其放在最后，并设置默认值为空"""
    if middle_name:
        full_name = first_name+' '+middle_name+' '+last_name
    else:
        full_name = first_name + ' ' + last_name
    print(full_name)


print('\n---实参可选---')
print_name('Jim','Green')
print_name('Anne','Hathaway','Jacqueline')


# 函数返回值:函数运算完毕，使用return返回的值
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print('\n---函数返回值---')
print(musician)

# 函数返回值可以是任何数据类型，比如字典
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('jimi', 'hendrix')
print('\n---函数返回值-字典---')
print(musician)
