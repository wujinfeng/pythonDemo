# 计算三角形面积
a = float(input('输入三角形第一边长：'))
b = float(input('输入三角形第二边长：'))
c = float(input('输入三角形第三边长：'))

while a + b < c or a + c < b or b + c < a:
    print('输入的边构不成三角形，请重新输入！')
    a = float(input('输入三角形第一边长：'))
    b = float(input('输入三角形第二边长：'))
    c = float(input('输入三角形第三边长：'))

p = (a + b + c) / 2
area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
print('三角形面积：%0.3f' % area)
