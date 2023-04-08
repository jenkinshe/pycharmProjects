import os
import re
import time

def find_filename(path):
    '定义一个获取获取最近一次修改文件的方法find_filename'
    file_names = os.listdir(path)
    # print(file_names)
    dict_file = {}
    for filename in file_names:
        if filename.endswith('.py'):
            file_path = path + '\\' + filename
            c_time = os.path.getctime(file_path)
            dict_file[filename] = c_time
    print(dict_file)
    #字典按照value排序
    item_list = [[item[1],item[0]] for item in dict_file.items()]
    # print(item_list)
    item_list.sort()
    print(item_list)
    return item_list[-1][1]


if __name__ == '__main__':
    path=input("请输入目录：")
    result_file = find_filename(path)
    # print(f"最近修改过的文件是：{result_file}")
    # print('最近修改的文件是：%s'%result_file)
    print('最近修改的文件是：{}'.format(result_file))






