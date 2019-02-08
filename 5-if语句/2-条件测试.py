# 每条if 语句的核心都是一个值为True 或False 的表达式，这种表达式被称为条件测试

# 在python中，= 表示赋值，即将右边的值赋给左边的变量
car = 'bmw'
# 使用 == 判断左右是否相等
car == 'audi'  # 不相等，此时car的值为bmw,该表达式运算结果为False
print(car == 'audi')  # False
car == 'bmw'
print(car == 'bmw')  # True

# 如果比较字符串时忽略大小写，那么统一转换成小写后比较
car1 = 'bmw'
car2 = 'BmW'
print(car1.lower() == car2.lower())  # True

# 检查不相等，使用 !=
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")  # 两个比较的字符串不相等，符合判断条件

# 比较数字  ==(等于)  !=(不等于)  <(小于)  <=(小于等于)  >(大于)  >=(大于等于)
age = 30
age > 18  # True
age == 30  # True
age < 18  # False
age >= 30  # True

