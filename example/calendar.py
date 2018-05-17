# 引入日历模块

import calendar

yy = int(input('输入年份：'))
mm = int(input('输入月份：'))

# 显示日历

print(calendar.month(yy, mm))
