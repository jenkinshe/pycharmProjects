# python元组
# 访问元组
tuple_1 =(50,20,6,9,8,'学习')
tuple_2 = ('yy','bobo')
print(tuple_1[0])
print(tuple_1[1:3])
print(tuple_2+tuple_1)
print(tuple_2*2)
# 修改元组
tuple_3= tuple_1+tuple_2
print(tuple_3)
# 删除元组
# del tuple_1    #删除元组tuple_1
# print(tuple_1)
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
list1=[1,2,3]
print(list1)
print(tuple(list1))   #输出将列表转换为元组
