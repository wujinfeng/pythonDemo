# 程序用于检测用户输入的数字是质数还是合数
import math

# 用户输入

num = int(input('输入一个数：'))

# 质数大于1

if num > 1:
    # 找到平方根
    square_num = math.floor(num ** 0.5)
    # 查找因子
    for i in range(2, square_num + 1):  # 将平凡根加1是为了能取到平方根那个值
        if (num % i) == 0:
            print(num, '是合数')
            print(i, '乘于', num // i, '是', num)
            break
    else:
        print(num, '是质数')
else:
    print(num, '既不是质数，也不是合数')
