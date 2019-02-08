# 使用range函数，第一个参数是开始值，第二个参数时结束值（不包含）
for num in range(1, 6):
    print(num)

# 使用range创建列表
print(range(1, 6))
# 需要使用list函数转换下
numbers = list(range(1, 6))
print(numbers)

# range第三个参数是数据间隔，默认是1，当设置为2时，可以打印区间范围内的奇数或偶数
print('---打印2-11之间的偶数---')
even_numbers = list(range(2, 11, 2))
print(even_numbers)
print('---打印3-12之间的奇数---')
odd_numbers = list(range(3, 12, 2))
print(odd_numbers)

print('---打印1到10的平方---')
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)

# 对于上面这种循环体只有一行代码且将原列表转化成新列表，可以使用列表推导，即下面的语法形式
print('---演示列表推导1---')
squares = [value**2 for value in range(1, 11)]
print(squares)
print('---演示列表推导2---')
names = [name.upper() for name in ['wyh','www','aaa']]
print(names)
