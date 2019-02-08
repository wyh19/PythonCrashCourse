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

# 遍历切片，和遍历列表是一样的
print('---打印前3名---')
for name in players[:3]:
    print(name)

# players列表赋值给其他变量，比如下面演示的a_players
a_players = players
print('---打印a_players---')
print(a_players)
#修改变量a_Players
a_players[0] = 'wyh'
# 查看列表的值
print('---修改后，打印a_players--')
print(a_players)
print('---打印原本--')
print(players)
print('---结论：原本受变量a_players改变的影响，因为两者指向同一个列表---')


# 使用切片赋值列表,即同时省略开头和结尾，得到一个完全相同的副本
copy_players = players[:]
print('---打印副本---')
print(copy_players)
#修改副本
copy_players[0] = 'wyh'
print('---修改后，打印副本--')
print(copy_players)
print('---打印原本--')
print(players)
print('---结论：原本不会受副本的影响，两者是各自独立的列表---')