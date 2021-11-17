# python 日期和代码
import time
# time.time() 获取当前时间戳
print(time.time())  #输出当前时间戳

# 获取当前时间
# time.localtime(time.time())  以时间戳方式向时间元组转换
print('本地时间为：',time.localtime(time.time()))

# 获取格式化时间
# time.asctime(time.localtime(time.time()))
print('本地时间为：',time.asctime(time.localtime(time.time())))

# 格式化日期 使用 time 模块的 strftime 方法来格式化日期
# time.strftime('时间格式',time.localtime())
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
print(time.strftime('%w %Y-%m-%d %H:%M:%S %j',time.localtime(time.time())))
# 将格式化字符串转换为时间戳
# time.mktime(time.strptime('格式化后的日期字符串',格式化类型))
a= '2021-09-24 15:11:42'
print(time.mktime(time.strptime(a,'%Y-%m-%d %H:%M:%S')))

# 获取某月日历
import calendar
print(calendar.month(1997,1))    #获取1997年1月的日历日期
print(calendar.month(2021,9))    #获取2021年9月的日历日期

#time模块
#日历模块
print(calendar.monthcalendar(2021,9))
print(calendar.weekday(2021,9,24))
