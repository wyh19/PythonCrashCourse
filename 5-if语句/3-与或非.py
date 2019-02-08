# Python中使用 and or not来表示逻辑运算的 与 或  非

# and的原则是两个条件都为True,运算结果才为true；只要有一个条件为False,结果就为False
age = 30
age > 20 and age < 50  # True and True :结果为True
age > 40 and age < 50  # False and True: 结果为False
age > 40 and age < 20  # False and False :结果为False

# or的原则是两个条件有一个为True，则结果为True;只有全为False时，结果才为False
age = 30
age > 20 or age < 50  # True or True :结果为True
age > 40 or age < 50  # False or True: 结果为True
age > 40 or age < 20  # False or False :结果为False

# not即取反，not True 为 False,not False 为 True
age = 30
not age > 20  # not True,结果为False
print(not age > 20)  # False
not age < 20  # not False ,结果为True

# 优先级
print(not age > 20 or age == 30)
