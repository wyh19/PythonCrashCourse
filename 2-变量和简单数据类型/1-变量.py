# 直接打印一段字符串
print('直接打印一段字符串')

# 使用变量关联一段字符串
message = '使用变量关联一段字符串'
# 打印变量，即打印这个变量关联的值
print(message)

"""
变量命名规范：
1、变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打头，例如，可将变量命名为message_1，但不能将其命名为1_message。
2、变量名不能包含空格，但可使用下划线来分隔其中的单词。Python的代码习惯是使用下划线连接单词，而不是其他语言惯用的驼峰式，
这一点最好入乡随俗，毕竟很多python的库都是这个命名规范。
3、不要将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的单词，如print。
4、变量名应既简短又具有描述性。例如，name比n好，student_name比s_n好，name_length比length_of_persons_name好。
5、慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0。
"""