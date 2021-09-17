#python条件语句

# if 条件：
#     print（）输出
# else：
#     print（）输出

# 实例： 输出小于7的整数
a=1
while a <9:
    if a < 7:
        print(a, 'a小于7')
    else:
        print(a, 'a大于7')
    a += 1     #循环递增

a=1
while a < 7:    #输出判断1-7奇数or偶数
    if (a %2==0):
        print(a,'is even偶数')
    else:
        print(a,'is odd奇数')
    a +=1

#多个条件elif用法
# if 条件：
#     print() 输出
# elif 条件：
#     print() 输出
# elif 条件:
#     print() 输出
# else:
#     print() 输出

num = 5  #实例：判断数字5是属于条件
if num == 3:
    print('bobo')
elif num == 2:
    print('憨憨')
elif num == 1:
    print('yy')
elif num <= 0:
    print('不喜欢')
else:
    print('喜欢')

# 由于python用法不能用switch，可以使用and、or、大于小于代替交差使用，达到多个条件同时满足效果
# 实例：判断值是否在0-2或大于22之间
num = 5
if (num > 0 and num < 2) or (num > 22):
    print(num,'符合的数字')
else:
    print(num,'不符合的数字')


num = 3
if num == 3: print('3');print('2') #后面可以在同一行输出print

# 更改数据增加 
