# 斐波那契数列实现

# 方法1
# num = int(input('你需要几项？'))
# f1 = 0
# f2 = 1
# if num <= 0:
#     print('请输入一个正整数')
# elif num == 1:
#     print('斐波那契数列：%d' % f1)
# else:
#     print('斐波那契数列：', end='')
#     print(f1, f2, end=' ')
#     for n in range(1, num - 1):
#         f = f1 + f2
#         f1, f2 = f2, f
#         print(f, end=' ')

# 方法2
# num = int(input('你需要几项？'))
#
# # 第一项和第二项
# n1 = 0
# n2 = 1
# count = 2
#
# # 判断输入的值是否合法
# if num <= 0:
#     print('请输入一个正整数')
# elif num == 1:
#     print('斐波那契数列：{}'.format(n1))
# else:
#     print('斐波那契数列：')
#     print(n1, ',', n2, end=' , ')
# while count < num:
#     nth = n1 + n2
#     print(nth, end=' , ')
#     # 更新值
#     n1 = n2
#     n2 = nth
#     count += 1

# 方法3
def fab(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n > 2:
        return fab(n - 1) + fab(n - 2)


def printFab(n):
    for i in range(1, n + 1):
        print(fab(i), end=' ')


num = int(input('你需要几项？'))

printFab(num)
