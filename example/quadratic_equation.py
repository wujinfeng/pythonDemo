# 二次方程式 ax**2 + bx + c = 0
# 输入a、b、c
# 输出 x 的解
# x1=(-b+sqrt(b**2-4ac))/2a
# x2=(-b-sqrt(b**2-4ac))/2a

# 导入cmath（复杂数学运算）模块

import cmath

a = float(input('输入a:'))
b = float(input('输入b:'))
c = float(input('输入c:'))

# 计算

d = (b ** 2) - (4 * a * c)

# 两种求解方式

sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

print('结果为{0} 和 {1}'.format(sol1, sol2))
