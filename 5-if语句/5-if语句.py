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
if age<4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")