# demo1:简单的传入列表
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ['hannah', 'ty', 'margot']
print('---demo1:函数使用列表---')
greet_users(usernames)

# demo2：一段没有使用函数的代码
print('\n---demo2：未使用函数的demo---')
# 首先创建一个列表
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron'] 
# completed_models用于保存已完成的
completed_models = []
# 模拟打印每个设计，直到没有未打印的设计为止
# 打印每个设计后，都将其移到列表completed_models中
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design) 
    completed_models.append(current_design)
# 显示打印好的所有模型
print("The following models have been printed:") 
for completed_model in completed_models:
    print(completed_model)

#
