# 判断列表是否为空,直接使用if判断，不为空则为True，否则为False
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
        print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?\n")


# 处理多个列表
# 定义店里有的配料列表
available_toppings = ['mushrooms', 'olives',
                      'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
# 定义客户需要的配料列表
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
# 遍历客户需求的配料
for requested_topping in requested_toppings:
    # 判断该配料是不是店里有的
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")
