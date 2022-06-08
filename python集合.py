# python集合 集合是无序和无索引的集合。在 Python 中，集合用花括号编写。.
# 构造函数 set()
set1={1,'dd','pp'}
print(set1)
# 将列表转换为集合
list1=[2,'hh','yy']
set2=set(list1)
print(set2)
# 更改集合元素  通过列表转换更改
set3={'xue','xi','jia','you'}
print('执行程序后的集合set3：',set3)              # 集合是无序的，所以每一次执行程序集合顺序都会更改
list2=list(set3)                              # 集合转换为列表
print('将set3转换为list2为：',list2)
list2[0:2]=[1,2]                              # 将索引下标为0-2的（前并后开）更改[1,2]
print('更改后的list2为：',list2)
set3=set(list2)                               # 将更改元素后的列表转换为集合
print('将list2转换为set3',set3)               # 打印转换元素后的集合

# 访问项目  for循环遍历或in查找是否存在
set3={'xue','xi','jia','you'}
for a in set3:
    print(a)
# 检查集合中是否存在
print('xue' in set3)
if 'xue' in set3:
    print("'xue'在set3中")
else:
    print('不在')

# 添加项目
# 添加一个项目add()
# 添加多个项目update()
thisset_1={"apple", "banana", "cherry"}
thisset_1.add('club759866')        # 添加一个项目add('club759866')
print('添加一个项目add后：',thisset_1)
# 添加多个项目update()
thisset_2={2, "banana", "cherry"}
thisset_2.update([3,'qq','ww','ee'])   # 添加多个项目update([3,'qq','ww','ee'])
print('添加多个项目update后',thisset_2)

# 获取set长度 len()
print(len(thisset_1))

# 删除项目  remove() discard() pop()
thisset_3={1,2,'uu','ii','oo','pp'}
thisset_3.remove('uu')      # 注释：如果要删除的项目不存在，则 remove() 将引发错误。
print('删除remove后thisset_3',thisset_3)
# discard
thisset_4={2,5,'yy','ty','ik'}
thisset_4.discard('ik')      # 注释：如果要删除的项目不存在，则 discard() 不会引发错误。
print('删除discard后thisset_3',thisset_4)
# 请记住，set 是无序的，因此您不会知道被删除的是什么项目。
#pop()  pop() 方法的返回值是被删除的项目。
thisset_5={'ww','ee','rr',2,5}
a=thisset_5.pop()              #pop()返回被删除的集合元素
print(a)
print('被删除元素a后集合thisset_5',thisset_5)


#clear() 清空集合内容
set4={5,'banban','club','winboh'}
set4.clear()
print('清空set4后为：',set4)
#del() 删除集合
# del set4
# print(set4)             #删除集合set4后，没有该集合，打印报错

#合并集合 union() update()
#update() update() 方法将一个集合中的所有项目插入另一个集合中：
set5={1,2,3}
set6={'jj','kk'',ll'}
set5.update(set6)        #将set6合并到set5中
print('打印合并后的set5',set5)
# union() union() 方法返回一个新集合，其中包含两个集合中的所有项目：
set7={5,6,7}
set8={'uu','io','op'}
set9 = set7.union(set8)   #将set7与set8合并返回新集合
print(type(set9)),print(set9)
