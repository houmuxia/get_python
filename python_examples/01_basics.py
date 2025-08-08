# -*- coding: utf-8 -*-

# 1. 变量和数据类型 (Variables and Data Types)

# 在Python中，你不需要显式声明变量的类型。
# 变量在第一次赋值时创建。

# 整数 (Integer)
age = 30
print("年龄 (整数):", age)

# 浮点数 (Float)
pi = 3.14159
print("圆周率 (浮点数):", pi)

# 字符串 (String)
name = "小明"
greeting = '你好, 世界!'
print("姓名 (字符串):", name)
print("问候 (字符串):", greeting)

# 布尔值 (Boolean)
is_student = True
is_working = False
print("是学生吗? (布尔值):", is_student)


# 2. 基本运算符 (Basic Operators)

# 算术运算符 (Arithmetic Operators)
a = 10
b = 3
print("\n--- 算术运算符 ---")
print("a + b =", a + b)  # 加法
print("a - b =", a - b)  # 减法
print("a * b =", a * b)  # 乘法
print("a / b =", a / b)  # 除法 (结果是浮点数)
print("a // b =", a // b) # 整除 (结果是整数)
print("a % b =", a % b)   # 取模 (余数)
print("a ** b =", a ** b) # 幂运算 (a的b次方)

# 比较运算符 (Comparison Operators)
x = 5
y = 10
print("\n--- 比较运算符 ---")
print("x == y:", x == y)  # 等于
print("x != y:", x != y)  # 不等于
print("x > y:", x > y)   # 大于
print("x < y:", x < y)   # 小于
print("x >= y:", x >= y) # 大于或等于
print("x <= y:", x <= y) # 小于或等于

# 逻辑运算符 (Logical Operators)
p = True
q = False
print("\n--- 逻辑运算符 ---")
print("p and q:", p and q) # 逻辑与
print("p or q:", p or q)  # 逻辑或
print("not p:", not p)     # 逻辑非


# 3. 简单的输入和输出 (Simple Input and Output)

# 使用 print() 函数进行输出
print("\n--- 输入和输出 ---")
print("Hello from Python!")

# 使用 input() 函数从用户那里获取输入
# input() 返回的是一个字符串
user_name = input("请输入你的名字: ")
print("你好,", user_name, "!")

# 如果需要接收数字，需要进行类型转换
user_age_str = input("请输入你的年龄: ")
user_age_int = int(user_age_str) # 将字符串转换为整数
print("你明年就", user_age_int + 1, "岁了。")
