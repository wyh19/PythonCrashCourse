user_0 = {
    'username': 'efermi', 'first': 'enrico', 'last': 'fermi',
}

# 字典通过items方法，得到一个列表
print('---字典转换成列表---')
print(user_0.items())
# 遍历字典列表
for key, value in user_0.items():
    print("Key: " + key)
    print("Value: " + value)

# 通过keys获得key列表
print('---通过keys获得key列表---')
print(user_0.keys())
# 遍历字典中所有的键
for key in user_0.keys():
    print(key.upper())
# 对key值排序
print('---对key值排序---')
for key in sorted(user_0.keys()):
    print(key.upper())

# 通过values获得value列表
print('---通过values获得value列表---')
print(user_0.values())
# 遍历字典中所有的值
for value in user_0.values():
    print(value.upper())


