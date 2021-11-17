#python 模块
#Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。
# 模块让你能够有逻辑地组织你的 Python 代码段。
# 把相关的代码分配到一个模块里能让你的代码更好用，更易懂。
# 模块能定义函数，类和变量，模块里也能包含可执行的代码。
def print_func(par):
   '输出字符内容'
   print('函数内布局变量：',par)
   return
print(print_func(2))

# 模块引入 使用import语句引入模块，‘import 模块’
# 调用模块中的函数时，使用 模块.函数，例如：support.sum1
# 从模块中导入具体的一部分到当前命名空间中 from 模块 import 具体部分
# 从模块中导入全部到当前命名空间 from 模块 import *

#python文件i/o
#读取键盘输入、input函数
str=input('请输入：')
print('你输入的内容是：',str)


