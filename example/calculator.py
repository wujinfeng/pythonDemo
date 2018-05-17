# 实现简单计算器实现，包括两个数基本的加减乘除

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        print('0不能作为分母')
        return
    else:
        return x / y


choice = int(input('请选择运算:\n1,相加\n2,相减\n3,相乘\n4,相除\n请输入运算(1/2/3/4):'))

num1 = float(input('请输入第一个数：'))
num2 = float(input('请输入第二个数：'))

if choice == 1:
    print('{}+{}={}'.format(num1, num2, add(num1, num2)))
elif choice == 2:
    print('{}-{}={}'.format(num1, num2, subtract(num1, num2)))
elif choice == 3:
    print('{}x{}={}'.format(num1, num2, multiply(num1, num2)))
elif choice == 4:
    print('{}/{}={}'.format(num1, num2, divide(num1, num2)))
else:
    print('选择的运算为非法输入')
