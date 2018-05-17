# 通过用户输入数字计算阶乘

# 方法1
# num = int(input('输入一个数字：'))
# factorial = 1
#
# # 查看数字是负数，0或正数
#
# if num < 0:
#     print('抱歉，负数无阶乘')
# elif num == 0:
#     print('0的阶乘是1')
# else:
#     for i in range(1, num + 1):
#         factorial = factorial * i
#     print('%d的阶乘为%d' % (num, factorial))
#

# 方法2
import math

num = int(input('请输入一个数字：'))
if num < 0:
    print('负数无阶乘')
else:
    print('{0} 的阶乘为 {1}'.format(num, math.factorial(num)))
