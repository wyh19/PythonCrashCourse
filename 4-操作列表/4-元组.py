# 元组是一组不可修改的列表数据，使用圆括号定义

# 元组和列表一样，可以使用索引访问
dimensions = (200, 50) 
print('---使用索引访问---')
print(dimensions[0])
print(dimensions[1])

# 元组和列表一样，可以遍历
print('---使用遍历---')
for d in dimensions:
    print(d)

# 不能修改元组,下面这句如果执行的话，会报错
# dimensions[0] = 1

# 但是可以修改指向元组的变量dimensions，使其指向其他值，因为变量本身并不是元组
dimensions = 1
print('---修改变量指向---')
print(dimensions)