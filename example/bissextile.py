# 判断是否为闰年

year = int(input('输入一个年份：'))
bissextile = False

if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            bissextile = True
        else:
            bissextile = False
    else:
        bissextile = True
else:
    bissextile = False

if bissextile:
    print('{0} 是闰年'.format(year))
else:
    print('{0} 不是闰年'.format(year))
