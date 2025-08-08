# -*- coding: utf-8 -*-

# 1. 条件语句 (Conditional Statements) - if, elif, else

print("--- 条件语句 ---")
score = 85

if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")

# 2. 循环语句 (Looping Statements)

# for 循环 (for loop)
# for循环通常用于遍历一个序列（如列表、元组、字符串）或范围。

print("\n--- for 循环 ---")

# 遍历一个列表
fruits = ["苹果", "香蕉", "樱桃"]
print("水果列表:")
for fruit in fruits:
    print(fruit)

# 使用 range() 函数
# range(5) 会生成从 0 到 4 的数字序列
print("\n打印 0 到 4:")
for i in range(5):
    print(i)

# range(start, stop, step)
print("\n打印 2 到 10 之间的偶数:")
for i in range(2, 11, 2):
    print(i)


# while 循环 (while loop)
# while循环会在给定条件为真(True)的情况下，重复执行一段代码块。

print("\n--- while 循环 ---")
count = 0
while count < 5:
    print("Count is:", count)
    count += 1 # 这等同于 count = count + 1


# 3. 循环控制语句 (Loop Control Statements) - break 和 continue

print("\n--- 循环控制 ---")

# break: 立即终止整个循环
print("使用 break 的例子:")
for i in range(10):
    if i == 5:
        break # 当 i 等于 5 时，跳出循环
    print(i)
print("循环结束")

# continue: 跳过当前迭代的剩余部分，直接进入下一次迭代
print("\n使用 continue 的例子:")
for i in range(10):
    if i % 2 == 0: # 如果 i 是偶数
        continue # 跳过当前迭代，不执行下面的 print
    print(i) # 只打印奇数
print("循环结束")
