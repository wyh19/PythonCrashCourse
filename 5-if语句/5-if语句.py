# if conditional_test:
#   do something
age = 19
print('---if演示---')
if age >= 18:
    print("You are old enough to vote!")

# if-else语句
age = 17
print('---if-else演示---')
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# if-elif-else演示
age = 12
print('---if-elif-else演示---')
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")

# 注意 elif可以使用多个，主要看判断条件的划分
# else 可以省略，如果不需要的话
print('---演示多个elif以及else省略---')
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 3
print("Your admission cost is $" + str(price) + ".")
