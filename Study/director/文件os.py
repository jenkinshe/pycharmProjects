import os
# os.mkdir('hhh')    #创建目录
# os.remove('kkk')    #删除文件
# os.rmdir('hhh')    #删除目录
# print(os.getcwd())   #获取当前目录的绝对路径
# print(os.listdir())   #以列表形式返回目录下所有文件及目录
# print(os.system('fdfd123'))
# print(os.path.abspath('文件os.py'))
# print(os.path.abspath('./'))
# print(os.path.abspath('./hhh'))
# print(os.path.exists('./hhh'))


#返回指定文件目录下的所有文件
def listdir(name):
    dirname_list = os.listdir(name)  #以列表形式返回文件目录下的所有文件
    print(dirname_list)
    for a in dirname_list:
        print(a)
#返回当前文件所在目录下的所有文件
def local_listdir():
    dirname_list=os.listdir()   #以列表形式返回文件目录下的所有文件
    print(dirname_list)
    for a in dirname_list:
        print(a)


def abs_path(name):
    a = os.path.abspath(name)
    print(a)

path = os.path.abspath('./hhh')
path_1 = os.path.abspath('tt.py')

def split_path_name(path):
    split_name = os.path.split(path)
    print(split_name)

def path_basename( path):
    basename = os.path.basename(path)
    print(basename)

def path_dirname( path):
    dirname = os.path.dirname(path)
    print(dirname)


# listdir(f'C:/Users/小Q/PycharmProjects/testApi/common')
# local_listdir()
abs_path('./hhh')
abs_path('tt.py')
split_path_name(path)
path_basename(path)
path_dirname(path)
split_path_name(path_1)
path_basename(path_1)
path_dirname(path_1)


