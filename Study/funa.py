'装饰器使用及被装饰函数有多个参数时装饰器使用'
import os

'1.被修饰的函数没有带参数，可以直接将funB作为funA（）的参数传入'
def funA(fn):
    fn()
    print('http://c.biancheng.net')
    return '装饰器返回值'

@funA
def funB():
    print('学习装饰器使用')
print(funB)

'2.被修饰的函数带参数，则需要在函数装饰器中嵌套一个函数，该函数带有的参数个数和被装饰器修饰的函数相同'

def funC(fn):
    def say(arc):
        print('这是一个装饰器里嵌套的一个函数',arc)
        fn('addd')
    return say
@funC
def funD(arc):
    print('dd')
funD('python')


'3.若有多个函数需要同个装饰器函数修饰，有些参数只有一个或多个，解决办法：*args和**kwargs作为装饰器内部嵌套函数的参数，' \
'*args 和 **kwargs 表示接受任意数量和类型的参数'

def funE(fn):
    def say(*args,**kwargs):
        fn(*args,**kwargs)
        print('ll',*args,**kwargs)
    return say

@funE
def funF(name,mobile):
    print('第一个被修饰的函数：',name,mobile)
@funE
def funG(arc):
    print('第二个被修饰的函数：',arc)

# funF('何',13233)
# funG('abc')




# def funA(fn):
#     print("C语言中文网")
#     fn() # 执行传入的fn参数
#     print("http://c.biancheng.net")
#     return "装饰器函数的返回值"
# @funA
# def funB():
#     print("学习 Python")
#
print(os.getcwd())
