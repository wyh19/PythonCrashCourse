# 使用列表自带的方法sort函数进行永久性排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars) # ['audi', 'bmw', 'subaru', 'toyota'] 

# 使用BIF的sorted函数进行临时排序，该函数不会改变列表本身，而是返回一个排序后的副本
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars_sorted  = sorted(cars)
print(cars_sorted) # ['audi', 'bmw', 'subaru', 'toyota']
print(cars) # ['bmw', 'audi', 'toyota', 'subaru'],列表本身没有变化

# 默认排序是按字母升序，降序需要指定参数reverse=True 
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars) # ['toyota', 'subaru', 'bmw', 'audi']

# 反转列表，即按索引顺序颠倒元素的顺序
cars = ['bmw', 'audi', 'toyota', 'subaru'] 
print(cars)
cars.reverse() 
print(cars)

# 使用BIF的len函数获取列表的长度
cars = ['bmw', 'audi', 'toyota', 'subaru'] 
print(len(cars))

# 注意：这里多次提到BIF,即Build In Funcitons,也就是语言的内置函数，这些函数可以直接拿来用，比如sorted
# 而像列表的sort函数，则是属于列表对象的,使用时，必须是列表对象.sort()的形式