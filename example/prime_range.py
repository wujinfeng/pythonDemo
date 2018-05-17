# 输出指定范围内的素数

import math

lower = int(input('输入区间最小值：'))
upper = int(input('输入区间最大值：'))

print('素数结果如下：')
print('=' * 10)

pri_num = 0
com_num = 0

for num in range(lower, upper + 1):
    # 找到平方根，减少算法时间
    square_num = math.floor(num ** 0.5)
    # 素数大于1
    if num > 1:
        for i in range(2, square_num + 1):
            if num % i == 0:
                com_num += 1
                break
        else:
            pri_num += 1
            print(num)  # 打印素数

print('=' * 10)
print(com_num, '个合数')
print(pri_num, '个质数')
