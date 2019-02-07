""" 
1、字符串就是一串文字，用引号括起来的都是字符串。
2、使用单引号或者双引号都可以，但是一定要成对使用
3、使用一种引号，比如单引号作为字符串的包括符，那么字符串内部的双引号将作为文字本身；反之亦然
4、字符串对象自带很多可操作函数，用于对本字符串进行函数运算
"""
# 定义一个字符串，赋值给变量name
name = "ada lovelace" 

# title函数，使其各单词首字母大写
print(name.title()) #输出 Ada Lovelace
# upper函数，使字符串全部大写
print(name.upper()) #输出 ADA LOVELACE
# lower函数，使字符串全部小写
print(name.lower()) #输出 ada lovelace


# 拼接字符串，使用+
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name) #输出 ada lovelace
message = "Hello, " + full_name.title() + "!" 
print(message) #输出 Hello, Ada Lovelace!

#使用\t增加缩进，使用\n换行
print('\tHello, \nWorld!')

# 删除首尾的空白字符:strip函数
msg = '  Hello World!  '
print(msg.strip())
# 只去除头部的空白
print(msg.lstrip())
# 只去除尾部的空白
print(msg.rstrip())
# 注意1：strip前面的l表示left,r表示right;也就是分别代表头与尾
# 注意2：到目前演示位置，函数并没有改变原字符串，而是得到一个新的字符串，因此msg依然是'  Hello World!  '