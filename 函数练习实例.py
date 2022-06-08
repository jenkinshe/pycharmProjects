##编写斐波那契数列的函数并调用
# def fib(n):##n是形参
#     a,b =1,1
#     while a<n:
#         print(a,end=' ')
#         a,b=b,a+b
#         print(a,b)
# fib(1000)



import 函数练习实例
def say_hello():
    '打印三次打招呼'
    print('哈喽你好啊1')
    print('哈喽你好啊2')
    print('哈喽你好啊3')
    return '结束'
# print(say_hello())   #调用打招呼函数say_hello
say_hello()




def my_function(child3, child2, child1):
  print("The youngest child is " + child3)
my_function(child1 = "Phoebe", child2 = "Jennifer", child3 = "Rory")


def sum_2_sum():
    '打印两参数相加'
    num1=1
    num2=1
    result=num1+num2
    print('%d + %d = %d'%(num1,num2,result))
    return '返回'
print(sum_2_sum())

def sum_3_sum():
    '打印两字符串相加'
    str1='今天'
    str2='天气很好'
    sum3=str1 + str2
    print('%s + %s = %s'%(str1,str2,sum3))
    return '结束'
print(sum_3_sum())     #局部变量调用函数
sum_3_sum()            #全局变量调用函数

def sum_4_sum(num3,num4):
    '参数传递给函数：打印两字符想加'
    result=num3+num4
    print('%d+%d=%d'%(num3,num4,result))
    print(result)
    return '结束'
print(sum_4_sum(3,4))

def poor_2_poor(num1,num2):
    '打印两参数相减'
    result=num1-num2
    print('%d - %d = %d'%(num1,num2,result))
    return '结束'
print(poor_2_poor(5,8))

def shang_1_shang():
    '打印量参数相除'
    num1=9
    num2=6
    shang1=num1/num2
    print('%d / %d = %d'%(num1,num2,shang1))
    return '结束'
print(shang_1_shang())

def take_1_take(num1,num2):
    '打印两参数之积'
    take1=num1*num2
    print('%d * %d =%d'%(num1,num2,take1))
    return '结束'
print(take_1_take(2.0,9))


#全局变量调用函数
take_1_take(3,9)    #调用函数take_1_take
sum_3_sum()         #调用函数sum_3_sum
函数练习实例.say_hello()  #调用函数练习实例文件下函数say_hello
sum_4_sum(5,9)
