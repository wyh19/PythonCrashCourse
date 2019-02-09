# 有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

# 由于列表和字典都是引用类型，即使拷贝了一份新的字典列表，两个列表里对应的字典依然只有一份，修改其中一个会影响两一个
# 拷贝一份字典列表
copy_aliens = aliens[:]
# 修改拷贝的列表第一项字典的color信息
copy_aliens[0]['color'] = 'wyhasd'
print('---修改副本第一项字典信息后，原本的第一项也受到影响---')
print(aliens[0])
# 直接修改副本第二项指向
copy_aliens[1] = {}
print('---修改副本第二项的指向，原本的第二项不会受到影响---')
print(aliens[1])
# 以上是值类型和引用类型修改的体现，一定要好好体会


# 创建一个用于存储外星人的空列表
aliens = []
# 创建30个绿色的外星人
for alien_number in range(0, 30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# 修改前面3个外星人信息
for alien in aliens[0:3]:
    alien['color'] = 'yellow'
    alien['speed'] = 'medium'
    alien['points'] = 10
# 显示前五个外星人
for alien in aliens[0:5]:
    print(alien)

# 字典中存储列表
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}
# 遍历字典
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    #遍历列表
    for language in languages:
        print("\t" + language.title())
