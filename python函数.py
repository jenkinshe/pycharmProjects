# python函数
def function(paraments):         #定义函数，输出文档
    '函数-文档字符串'
    print(paraments)
    return 0
print(function('挽回不如看成是重新追求'))   #调用函数
print(function(paraments='用心真诚信任、知行合一'))   #调用函数

#关键字参数
def printinfo(name,age):         #定义函数-打印名字与年龄
    '打印任何传入参数的字符串'
    print('age:', age)
    print('name:', name)
    print('age:',age,'name:',name)
    return '加油'
print(printinfo(age=24,name='游承燕'))   #调用函数，关键字参数允许函数调用时参数的顺序与声明时不一致

#默认参数
def printinfo(age=24,name='youchengyan'):   #传入默认参数值age、name
    '打印任何传入的字符串'
    print('name:',name,'age:',age)
    print('name:',name)
    return 'hola'
print(printinfo(age=25,name='何庆'))
print(printinfo(age=22))                #调用函数时，默认参数的值如果没有传入，则被认为是默认值,name未被传入，则调用默认值
print(printinfo(name='承'))             #age参数值未被传入，则调用默认值

#不定长参数
def printinfo(arg1,*situe):
    '不定长参数，打印任何传入的参数'
    print('输出：')
    print(arg1)
    for a in situe:
        print(a)
    return 0
print(printinfo(70))
print(printinfo(1996,1211,1997,119))

def printinfo1(arg2,*name):    #加了星号（*）的变量名会存放所有未命名的变量参数
    print('输出:')
    print(arg2)
    for b in name:
        print(b)
    return 1
print(printinfo1(22))
print(printinfo1(1998,319,222))

#匿名函数
#return语句
def sum(arg1,arg2):
    '两个参数相加'
    sum=arg1+arg2
    print('两个参数相加值:',sum)
    return sum           #选择性地向调用方返回一个表达式,不带参数值的return语句返回None
print(sum(22,12))

#全局变量与局部变量
#定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
#局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问
total=11
def sum1(arg1,arg2):
    '两个参数相加'
    sum1=arg1+arg2
    print('函数内是局部变量:',sum1)
    return 0
print('函数外的局部变量:',total)      #全局变量
print('函数内的局部变量:',sum1(1,2))  #局部变量


