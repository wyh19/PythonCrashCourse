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