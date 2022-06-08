# python字典
# 创建字典
dict1={'lover':'燕燕','dislover':'啵啵','moment':'2021.9.01'}
dict2={'key':'value','student':'何庆','teacher':'yy'}
# 构造函数 dict()
thisdict = dict(brand='Porsche', model='911', year=1963)   # 请注意，关键字不是字符串字面量 使用了等号而不是冒号来赋值
print(thisdict)
# 访问字典的值 键值对、get()
print('键lover对应的值',dict1['lover'])
print(dict1['lover']+dict2['teacher'])
# a = dict1.get('dislover')       #利用get获取dict1中dislover中的值
# print(a)
print('利用get获取dislover键中的值：',dict1.get('dislover'))
print(dict1,dict2)
# 修改字典
dict1['moment']='1996.12.11'   # 更改moment键对应的值
dict1['时间']='2021.9.01'       # 添加键值对，时间，dict1中没有键，则为添加
print(dict1)
list1=[1,2,3]
dict1['hh']=list1             # 添加键值对，hh值为列表
print(dict1)
tuple1=(1,2,3)
dict1['yy']=tuple1            # 添加键值对，yy值为元组
print('添加元组yy后的dict1：',dict1)

# 遍历字典 for循环遍历
for x in dict2:
    print('dict2中的键：',x)                  #遍历字典dict2中的key
for x in dict2:
    print('遍历dict2中的values1：',dict2[x])   #遍历字典dict2中的values
# 您还可以使用 values() 函数返回字典的值
for x in dict2.values():
    print('遍历dict2中的values2',x)           #遍历字典dict2中的values
# 通过使用 items() 函数遍历键和值
for x in dict2.items():
    print('遍历dict2中的键值对',x)             #遍历dict2中的键值对
# 检查建是否存在
dict2={'key':'value','student':'何庆','teacher':'yy'}
if 'key' in dict2:
    print('"key"在字典dict2中')
else:
    print('"key"不在字典dict2中')
# 获取字典长度 len()
print('字典dict2长度：',len(dict2))



# 删除字典 pop()、popitem()、del()、clear()
# del dict1['时间']              #删除字典键是时间的键值对
# print(dict1)
# dict1.clear()                 #清空字典所有条目
# print(dict1)
# del dict1                   #删除字典
# print(dict1)

# pop() 方法删除具有指定键名的项
thisdict_1={"brand": "Porsche","model": "911","year": 1963}
a = thisdict_1.pop('brand')              # 删除thisdict_1中指定键名brand项
print(a)                                 # 打印被删除brand键的值
print('删除指定键brand后的字典thisdict_1',thisdict_1)

# popitem() 方法删除最后插入的项目（在 3.7 之前的版本中，删除随机项目）
thisdict_2={'pp':'bobo','kk':'ll','hh':222}
b = thisdict_2.popitem()                # 删除thisdict_2中最后一项键值对
print(b)                                # 打印被删除的键值对
print('被删除最后一项键值对后的thisdict_2：',thisdict_2)

# 删除字典中指定项 del dict[x]
thisdict_3 = {'key':'value','student':'何庆','teacher':'yy'}
del thisdict_3['key']                   # 删除指定项key
print('删除指定项key后thisdict_3:',thisdict_3)

# 删除字典 del dict
# del thisdict_3
# print(thisdict_3)                       # 字典thisdict_3被删除后打印无

# 清空字典clear()
thisdict_3.clear()
print('被清空后的字典thisdict_3:',thisdict_3)


# 复制字典copy()、 dict()
# 复制字典 copy() 使用 copy() 方法来复制字典 dict()
thisdict_4 = {"brand": "Porsche","model": "911","year": 1963}
mythisdict= thisdict_4.copy()             # 复制thisdict_4并返回新字典mythisdict
print('复制的字典muthisdict:',mythisdict)
# 制作副本的另一种方法是使用内建方法 dict()
thisdict_5 = {"model": "911","year": 1963}
mydict = dict(thisdict_5)                 # 复制字典thisdict_5并返回给新字典mydict
print('复制thisdict_5返回给新字典mydict:',mydict)


# 嵌套字典 字典包含多个字典
child1 = {"name" : "Phoebe Adele","year" : 2002}
child2 = { "name" : "Jennifer Katharine", "year" : 1996}
child3 = { "name" : "Rory John","year" : 1999}
child = {'child1':child1,'child2':child2,'child3':child3}
print(child)
# 注意事项
# 字典键的特性
dict2={'key':'value','student':'何庆','teacher':'yy','student':'燕y'}     #不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
print(dict2)
print(dict2['student'])
# 键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行
dict3={(1,2,3):'元组','tt':'shuzi'}                                    #元组充当键
print(dict3)
# dict4={[1,2,3]:'列表','tt':'shuzi'}                                  # 列表充当键
# print(dict4)
dict5={'zifuchuan':'字符串','shuzi':(1,2,3)}                           #字符串充当键
print(dict5)
print(dict5['shuzi'])

# 字典内置函数及方法
# 函数cmp、len、str、type
print(len(dict5))    #计算键的总数，计算字典元素个数
print(type(dict5))   #输出字典类型
print(str(dict5))    #输出字典可打印的字符串表示
# 方法
dict3={(1,2,3):'元组','tt':'shuzi'}
dict5={'zifuchuan':'字符串','shuzi':(1,2,3)}
# dict.clear()清除
dict5.clear()       #删除字典内所有的元素，清空字典的所有条目
print(dict5)

# dict.copy()复制
dict3.copy()       #返回一个字典的浅复制
print('dict3的浅复制为：',dict3)
# dict.fromkeys(seq,val) #创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
a=dict.fromkeys('yyky',2)           #创建新字典a，键分别为yk，值为2
print(a)
print(dict.fromkeys('yb',(1,2,3)))  #创建新字典，键分别为yb，值都为元组（1,2,3）
# dict.get()返回指定值
dict3={(1,2,3):'元组','tt':'shuzi'}
a=dict3.get((1,2,3),'k')            #返回指定值（键对应值），若值不在字典中，返回default值（‘k'）
print(a)
print(dict3.get('hh','woxihuan'))   #键hh不存在字典中，返回default值为’woxihuan‘

# dict.setdefault() 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
y=dict3.setdefault('tt','heqing')   #键tt存在字典dict3中，返回字典键对应的值’shuzi‘
print('存在键tt对应的值',y)
h=dict3.setdefault('hh','喜欢')     #键hh不存在字典dict3中，新增加键hh且返回default值’喜欢‘
print('不存在键hh对应的值',h)
print('新增键hh后的字典',dict3)

# get与setdefault区别
# setdefault 如果不存在会在原字典里添加一个 key:default_value 并返回 default_value。
# get 找不到 key 的时候不会修改原字典，只返回 default_value。

# dict.has_key()  Python 3.X 不支持该方法

# dict.items()  #以列表返回可遍历的(键, 值) 元组数组
dict3={(1,2,3):'元组','tt':'shuzi'}
print(dict3.items() )              #将dict3字典中键值对组成一个元组，并把这些元组放在列表中返回
for key,values in dict3.items():   #遍历dict3中的key，values
    print(key,values)
for b in dict3.items():            #遍历dict3中的元组
    print(b)

# dict.keys()   #以列表返回一个字典所有的键
print(dict3.keys())

# dict.values() #以列表返回字典中的所有值
print(dict3.values())

# dict.update(dict1) #将字典dict1中的键值对更新到字典dict中
dict4={'同事':'yangzai','老师':'huazai'}
dict={'学生':'hazai'}
dict.update(dict4)     #将字典dect4中的键值对更新到dict中
print(dict)

# dict.pop() #删除键值对
dict6={'机会':'有','成功':'可以','失败':'不可以'}
dict6.pop('失败')       #删除字典中中key为失败的键值对
print(dict6)
dict6.setdefault('加油','努力')   #新增键值对
print(dict6)
print(dict6.pop('加油'))         #删除键值对‘加油’，返回对应值
print(dict6)

# dict.popitem() #返回并删除字典中最后一对键值对
dict7={'燕燕':'yy','啵啵':'bobo'}
print(dict7.popitem())     #返回字典中最后一对键值对，并删除最后一对键值对
print(dict7)               #删除字典中最后一对键值对后的字典


