print('你好，燕燕')
i=[1,3,2,5]
a=1
if a in i:
    print("b");print('d')
else:
     print("c")

a=[1,2,3,4,5,6,8]
b=[9]
print(a)
print(type(a))
print(a+b)

# 换行,多行语句，注意[]、{}、()不用\符号就可进行换行
a=1+\
    2+\
    3
print(a)
a=['mondays','tuesdays','wednedays',
   'thuesdays','fridays']

# 单行引号’，“,多行引号""" 内容 """ 可以换行
page="""
这是一段话"""
print(page)

# 注释、多行注释
# 多行注释：''' 内容 '''，“”“ 内容 ”“”可以注释其中内容
'''
print(a)
a=10
'''

a=2
b=3
print(a,b)
print(a);print(b)
# 多个变量赋值
a,b,c=1,2,'燕燕'
print(a)
print(b)
print(c)
print(a,b,c)

var_a='忘不掉燕燕'
print(var_a)
# del var_a   #del语句删除对象的引用
# print(var_a)

#python字符串
str='nishuo ni bu xihuan wo'
yy='燕燕'
print(str[2]) #输出下标为2的字符
print(str[:]) #输出全部字符
print(str[2:9])#前并后开，输出下标从2到9的字符
print(str[-6:-1]) #前并后开，从右往左数，输出从右往左第六位到第一位的字符
print(str[-1]) #输出从右往左数第一位字符
print(str+yy) #输出连接的字符串
print(str*2+yy) #输出字符串两次且连接字符串，*表示输出字符串多次|重复输出
print(str[1:7])
print(str[1:6:2]) #步长

# python列表
yy=[1996,12,11,'生气','痛苦','开心']
bobo=[1998,2,22,'痛苦','值得','可爱']
# yy[2]=9 列表赋值
print(yy[0:3]) #前并后开，输出下标从0到3的元素列表
print(yy[-3:-1]) #前并后开，从右往左数，输出下标从-3到-1的元素列表
print(yy[1]) #输出下标为1的元素列表
print(yy[-1]) #输出下标为-1的元素列表
print(yy*2) #重复输出yy列表里两次
print(yy+bobo) #输出yy与bobo的连接元素列表|组合列表

# python元组
qq=(1,9,10,'很气人','很值得')
yy=(9,3,5,'很可爱','很温柔','很漂亮')
print(qq)
# qq[2]=6  元组不能用来赋值
# print(qq)
print(qq[1:5]) #前并后开，输出下标从1到5的元素元组
print(qq[-3:-1]) #前并后开，从右往左数，输出下标从-3到-1的元素元组
print(yy[3]) #输出下标为3的元素元组
print(yy[-2]) #输出下标为-2的元素元组
print(yy+qq) #输入yy与qq元组的连接元组
print(yy*2) #输出yy列表的重复元组两次

# python字典
dict={}
print(dict)
dict[1]={'one'}
print(dict[1]) #输出键为1的值
dict_one={'xihuan':'燕燕','yy':'bobo','tz':'挽回'}
print(dict_one) #输出完整的字典
print(dict_one.keys()) #输出所有key键
print(dict_one.values()) #输出所有value值
print(dict_one['xihuan'])  #输出key键对应的value值

# python算数运算符
a = 21
b = 10
c = 3
print(c)

c = a + b
print('1_c 的值为：', c) #运算符+
c = a - b
print('2_c 的值为：',c) #算数运算符-
c = a * b
print('3_c 的值为：',c) #算数运算符*
c = a ** b
print('4_c 的值为：',c) #算数运算符次方，冥
c = a / b
print('5_c 的值为：',c) #算数运算符除/
c = a % b
print('6_c 的值为：',c) #算数运算符取模取余数%
c = a // b
print('7_c 的值为：',c) #算数运算符取整数，返回商的整数部分，向下取整

a = 21
b = 12
c = 3

c = a = b #赋值，b赋值给a，a赋值给c
print(a)  #输出a的值
print('8_c 的值为：',c)

# python比较（关系）运算符
a = 21
b = 12
c = 3
if a == b:     #等于运算符
    print('1_a等于b')
else:
    print('1_a不等于b')

if a != b:    #不等于运算符
    print('2_a不等于b')
else:
    print('2_a等于b')

if a > b:    #大于运算符
    print('3_a大于b')
else:
    print('3_a小于等于b')

if a < b:   #小于运算符
    print('4_c小于b')
else:
    print('4_c大于等于b')

#python赋值运算符
a = 21
b = 10
c = 0
c = a + b
print('1_c的值为：',c)  #输出赋值+

c +=a
print('2_c的值为：',c)  #输出赋值+

c *=a
print('3_c的值为：',c)  #输出赋值*

c /=a
print('4_c的值为：',c)  #输出赋值/，除

c -=a
print('5_c的值为：',c)  #输出赋值-

c %=a
print('6_c的值为：',c)  #输出赋值取余，%

a = 3
c //=a
print('7_c的值为：',c)  #输出赋值商取整，向下取整

a =-3
c =10
c //=a
print('8_c的值为：',c)  #输出赋值商取整，向下取整

a =2
c =3
c **=a
print('9_c的值为：',c)  #输出赋值冥次方，**

#python位运算符   按照二进制计算
#python逻辑运算符  and、or、not
#python成员运算符   in、not in
#python身份运算符  is、is not









