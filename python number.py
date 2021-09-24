import math
import string

var_1 = 10
var_2 = 9

print(var_1,var_2)
# del var_1   #删除对象
# print(var_1,var_2)
# python支持四种不同的数值类型：整数、长整数、浮点型、复数
int = 10
long = 9
float = 8
complex = 7

# python number类型转换
int_c = 9
print(type(int_c))


# python math、cmath模块包含了数学运算函数，math是浮点数数学运算、cmath是复数数学运算
import cmath
import math
dir(cmath)
dir(math)
print(cmath.sqrt(-1))
print(cmath.sin(9))
print(math.sin(9))

# python数学函数
# python随机数函数
# python三角函数
# python数学常量  pi（圆周率π，自然常熟e）

#python字符串
a = '好好学些，调整心态，充实自己'
b = '陪伴是最长情的告白'
print('a[0]值为：',a[0])        #输出字符串索引下标为0的值
print('a[1:3]的值为：',a[1:3])  #输出字符串索引下标为1-3的值，前并后开
print(a+b)                    #连接字符串a b
print('a[0]+a[1:3]的值为：',a[0]+a[1:3])    #输出字符串索引下标为0与下标为1-3前并后开的值，连接并输出
print(a+b*2)                  #输出a与b的两倍连接
print(b+'  --何庆')            #输出b连接字符串

# python转义字符 在需要在字符中使用特殊字符时，python 用反斜杠 \ 转义字符
#python字符串运算符
a = 'hello'
b = 'world'
print(a+b)
print(a[0])
print(a[:])
print('h' in a)   #成员运算符，判断字符h是否再字符串a中
print('h' in a and 'w' not in b)     #and、or逻辑运算符，in、not in成员运算符，判断h在字符串a中且w不在字符串b中成立
if 'h' in a:
    print('h在字符串a中')
else:
    print('h不在字符串b中')

print(r'\n')

# python字符串格式化
print('my name is %s and weight is %d kg' %('何庆',52))   #%d格式化整数、%s格式化字符串
a = 'her name is %s and weight is %d kg'
print(a %('游承燕',48))

# python三引号
yy = '''YCY\nHQ'''              #加\n可换行，单引号三引号中都可换行
print(yy)
print('''ycy\nhq''')            #加\n可换行，单引号三引号中都可换行
print('youchengyan\nheqing')    #加\n可换行，单引号三引号中都可换行
YY_1 = '''YCY     #三引号''''''可换行
HQ'''
print(YY_1)
print('''YCY      #三引号''''''可换行
HQ''')

# Unicode 字符串
print(u'hello world')

# python的字符串内建函数
# var_3 = 'Youchengyan'
# print(string.capwords(var_3))
# print(string.lower(var_3))

