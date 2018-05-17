# 实现最大公约数算法

# 定义一个函数
def hcf(x, y):
    """该函数返回两个数的最大公约数"""
    hcf = ''
    # 获取最小值
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i

    return hcf


# 用户输入2个数字
num1 = int(input('输入第一个数：'))
num2 = int(input('输入第一个数：'))

gcd = hcf(num1, num2)

print(num1, '和', num2, '最大公约数为', gcd)
