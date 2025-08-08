# -*- coding: utf-8 -*-

# 函数 (Functions) 是组织好的、可重复使用的，用来实现单一，或相关联功能的代码段。
# 函数能提高应用的模块性，和代码的重复利用率。

print("--- 函数 ---")

# 1. 定义和调用函数 (Defining and Calling Functions)

# 使用 `def` 关键字定义一个函数
def say_hello():
    """这是一个简单的函数，用于打印问候语。"""
    print("你好，欢迎学习Python函数!")

# 调用函数
print("调用 say_hello() 函数:")
say_hello()


# 2. 带参数的函数 (Functions with Parameters)

def greet_user(name):
    """这个函数接受一个名字作为参数，并打印个性化的问候语。"""
    print(f"你好, {name}!") # f-string 是一种方便的字符串格式化方法

print("\n调用带参数的函数:")
greet_user("小王")
greet_user("小李")


# 3. 返回值的函数 (Functions with Return Values)

def add_numbers(a, b):
    """这个函数接受两个数字作为参数，并返回它们的和。"""
    return a + b

print("\n调用带返回值的函数:")
sum_result = add_numbers(5, 3)
print("5 + 3 =", sum_result)
print("10 + 20 =", add_numbers(10, 20))


# 4. 默认参数值 (Default Parameter Values)

def describe_pet(pet_name, animal_type="狗"):
    """
    这个函数描述一个宠物。
    animal_type 有一个默认值 '狗'。
    """
    print(f"\n我有一只{animal_type}。")
    print(f"它的名字叫{pet_name}。")

print("\n调用带默认参数的函数:")
# 使用默认值
describe_pet("旺财")
# 提供新的值
describe_pet("咪咪", "猫")


# 5. 关键字参数 (Keyword Arguments)

# 你可以使用 `key=value` 的语法来传递参数，这样可以忽略参数的顺序。
def subtract(a, b):
    return a - b

print("\n使用关键字参数:")
# 顺序不重要
result1 = subtract(a=10, b=3)
result2 = subtract(b=3, a=10)
print("subtract(a=10, b=3) =", result1)
print("subtract(b=3, a=10) =", result2)

# 位置参数和关键字参数混用 (位置参数必须在前)
result3 = subtract(10, b=3)
print("subtract(10, b=3) =", result3)


# 6. 变量的作用域 (Variable Scope)

global_var = "我是一个全局变量"

def scope_test():
    local_var = "我是一个局部变量"
    print("\n--- 变量作用域 ---")
    print("在函数内部访问全局变量:", global_var)
    print("在函数内部访问局部变量:", local_var)

scope_test()

print("在函数外部访问全局变量:", global_var)
# 下面这行代码会报错，因为 local_var 是局部变量，在函数外部无法访问
# print("在函数外部访问局部变量:", local_var) # 取消注释这行会看到 NameError
