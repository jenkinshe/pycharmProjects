import os

#获取指定目录下文件并对每一个文件生成绝对路径,并对绝对路径进行分割
def get_director(name_path):
    directors_list=os.listdir(name_path)
    aa = []
    bb = []
    cc = {}
    dd = []
    for director_s in directors_list:
        juedui=os.path.abspath(director_s)
        split_path=os.path.split(juedui)
        aa.append(split_path[1])
        bb.append(split_path[0])
        cc[juedui] = split_path
        dd.append(split_path)
        # return director_s,juedui,split_path
        # print(director_s)
        # print(juedui)
        # print(split_path)
        hh =f"你想要返回的路径是{dd}"
    return hh

# def get_director(name):
#     directors_list=os.listdir(name)
#     for director_s in directors_list:
#         print(director_s)


if __name__ == '__main__':
    name_path =input("请输入你想知道的指定目录路径：")
    A = get_director(name_path)
    print(A)



