# 列表 由一系列按特定顺序排列的元素组成。使用[]表示，其中的各元素间使用逗号分隔
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)  # 打印结果包含方括号

# 访问列表元素，即索引，第一项索引为0，依次增加
print(bicycles[0])  # trek
print(bicycles[2].title())  # Redline
# 最后一项的索引为 -1
print(bicycles[-1].upper())  # SPECIALIZED

# 修改、添加和删除元素，注意这些操作会改变列表的元素，因此每次演示新的例子，都重新给变量赋值初始的列表
motorcycles = ['honda', 'yamaha', 'suzuki']
# 通过给指定索引赋值，修改其原有的值
motorcycles[0] = 'ducati'
print(motorcycles)  # 输出 ['ducati', 'yamaha', 'suzuki']

# 使用append在末尾添加元素
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)  # 输出['honda', 'yamaha', 'suzuki', 'ducati']
# 使用insert插入元素，该函数需要指定插入的位置，原来该位置的元素往右移动一位
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(1, 'ducati')
print(motorcycles)  # 输出 ['honda', 'ducati', 'yamaha', 'suzuki']

# 列表的pop函数，从末尾弹出元素
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles) # ['honda', 'yamaha']
print(popped_motorcycle) # suzuki

# pop弹出任何位置的元素，需要指定索引
motorcycles = ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop(1)
print(motorcycles) # ['honda', 'suzuki']
print(popped_motorcycle) # yamaha

# 根据值删除元素,使用remove函数，该函数只删除第一次匹配的值，如果需要删除全部符合的值，需要使用遍历
motorcycles = ['honda', 'yamaha', 'suzuki'] 
motorcycles.remove('yamaha') 
print(motorcycles) #['honda', 'suzuki']
