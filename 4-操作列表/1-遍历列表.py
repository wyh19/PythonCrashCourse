# 使用Python的for循坏遍历列表
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
# 仔细研究上面的流程，首先从列表magicians中取出第一个元素‘alice’赋值给magician变量，然后进入循环体执行print代码；
# 循环体是for语句下缩进一级的代码
# 然后继续执行下一个元素，直到所有元素都执行过了，循环结束

# 循坏体执行更多代码
print('----演示循坏体执行更多代码----')
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

# 循环结束后
print('----演示循环结束后----')
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians:
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
    print(magician.title() + ", that was a great trick!")
# 注意：下面这句代码没有缩进，意味着是循环体外的代码，也就是循环结束才执行
print("Thank you, everyone. That was a great magic show!")
