# python元组 元组是有序且不可更改的集合。在 Python 中，元组是用圆括号编写的。
# 访问元组
tuple_1 =(50, 20, 6, 9, 8, '学习')
tuple_2 = ('yy', 'bobo')
print(tuple_1[0])
print(tuple_1[-4:-1])
print(tuple_1[-6:-1])
print(tuple_1[1:3])
print(tuple_2+tuple_1)
print(tuple_2*2)
# 修改元组
# 创建元组后，您将无法更改其值。元组是不可变的，或者也称为恒定的。
# 但是有一种解决方法。您可以将元组转换为列表，更改列表，然后将列表转换回元组。
tuple_3=(1,2,'fd','hh')
list1=list(tuple_3)  #将列表转换为元组
print(list1)         #打印转换的列表
list1[0]='love'      #更改列表元素值
print(list1)         #打印更改后的列表
tuple_3=tuple(list1) #将已更改元素值的列表转换为元组
print('更改后的元组',tuple_3)       #打印更改后的元组

# 合并元组
tuple_4= tuple_1+tuple_2
print(tuple_4)
# 删除元组
# 注释：您无法删除元组中的项目。
# 元组是不可更改的，因此您无法从中删除项目，但您可以完全删除元组：
# del tuple_1    #删除元组tuple_1
# print(tuple_1)
# 创建元组 构造函数tuple()
# 一：
thistuple_1=tuple((1,2,'student','teacher'))
print(thistuple_1)
# 二：
tuple_5=(2,5,'dfd','yy','hq')
thistuple_2=tuple(tuple_5)
print(thistuple_2)



#列表转换为元组
list1=[1,2,3]
print(list1)
print(tuple(list1))   #输出将列表转换为元组
# 元组运算符
print(len((1,2,5)))      #计算元素个数
print(tuple_1+tuple_2)   #连接
print(tuple_2*2)         #复制、重复
print('yy' in tuple_2)   #判断元素是否存在
for a in tuple_2:print(a)  #迭代，遍历元组tuple_2中各元素
#元组内置函数 cmp、len、max、min
print(max(3,6,9))
print(min(1,4,7))
print(len((7,8,9)))

#判断元素是否在元组中
tuple_2 = ('yy','bobo')
if "yy" in tuple_2:
    print('"yy" 在元组中')
else:
    print('“yy”不在元组中')

