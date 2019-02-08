# 字典就是一组键值对数据，使用{}表示
info = {'name': 'wyh', 'age': 30}
print(info)
# 注意，不同于js中的对象，python中的key必须使用字符串

# 使用[key]访问字典中的值
print(info['name'])

# 添加或修改信息，已存在的信息则修改，不存在则添加
info['gender'] = '男'
print(info)
info['name'] = 'wyh19'
print(info)

# 删除键值对，使用del语句
del info['gender']
print(info) # 删除了性别信息


