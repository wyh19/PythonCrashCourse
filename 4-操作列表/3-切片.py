# 切片，即获取列表的一部分，与函数range() 一样，Python在到达你指定的第二个索引前面的元素后停止。
players = ['charles', 'martina', 'michael', 'florence', 'eli']
# 打印索引0，1，2 （3不包含）
print('---打印索引0，1，2 切片得到的列表（副本）---')
print(players[0:3])
# players列表本身没有变化
print('---players列表本身没有变化---')
print(players)

# 如果省略第一个索引，则从头开始；省略第二个索引，则到结尾（含结尾）
print('---演示省略开始索引---')
print(players[:3])
print('---演示省略结尾索引---')
print(players[1:])