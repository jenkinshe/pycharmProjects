import  os
import sys
# #获取文件路径
# os.getcwd()   #获取当前目录绝对路径
# print(os.getcwd())
# a = sys.path[0]    #输出当前执行的py文件所在的绝对路径
# print(a)
# print(os.listdir())   #返回指定目录下所有的目录和文件
# listdirname = os.listdir()
# for filename in listdirname:
#     print(filename)
# file_path = './common/'+'/wenjian'+'.py'
# file_path_1 = './common/fdsfd'
# file_path_2 = 'case'
# print(os.path.abspath(file_path))     #输出文件的绝对路径
# print(os.path.abspath(file_path_1))   #输出目录的绝对路径
# print(os.path.abspath(file_path_2))   #输出目录的绝对路径


#打开文件并执行文件操作
context = 'a+...hei,The computer grade examination is divided into four levels.\n 这是第二行内容\n 这是第三行内容 '
e = open('C:/Users/小Q/PycharmProjects/testApi/common/fdsfd','w')
e.write(context)
e.close()
ll = []
with open(f'C:/Users/小Q/PycharmProjects/testApi/common/fdsfd','r') as f:
    # for a in f:
    #     b = a[:-1]
    #     if b not in ll:
    #         ll.append(b)
    # print(ll)
    # aa = f.read()
    # print(aa)
    # print(f2)
    # f3=f.readlines()
    # print(f3)
    # print(f.read())
    print(f.readlines())
    # for a in f.readlines():
    #     b=  a[:-1]
    #     print(b)
    # print(f.read())

context_1 = f"\n2555gfgfgfgfg\tfgfgfgf"
with open(f'C:/Users/小Q/PycharmProjects/testApi/common/fdsfd','a',encoding='utf-8') as f:
    f.write(context_1)
with open(f'C:/Users/小Q/PycharmProjects/testApi/common/fdsfd','r') as f:
    # f.read()
    # print(f.read())
    # print(f.readline())
    # print(f.readlines())
    a=f.readlines()
    print(a)
#判断新增的一条数据是否成功新增到最后一行
    if a[3]=='2555gfgfgfgfg\tfgfgfgf':
        print('新增的数据成功新增')
    else:
        print('未成功新增或其他异常')




