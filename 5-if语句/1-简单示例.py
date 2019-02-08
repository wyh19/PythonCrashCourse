# 编程时经常需要检查一系列条件，并据此决定采取什么措施。
# 在Python中，if 语句让你能够检查程序的当前状态，并据此采取相应的措施。

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper()) 
    else:
        print(car.title())

# 在上面的例子中，将bmw打印成纯大写，其他的打印成成首字母大写