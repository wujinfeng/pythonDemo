#!/usr/bin/python3

#fibonacci series :斐波纳qi数列
#两个元素的总和确定了下一个数

a,b = 0, 1
while b < 1000:
	print(b, end=",")
	a,b = b, a+b

