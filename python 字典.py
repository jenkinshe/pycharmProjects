# python字典
# 创建字典
dict1={'lover':'燕燕','dislover':'啵啵','moment':'2021.9.01'}
dict2={'key':'value','student':'何庆','teacher':'yy'}


# 访问字典的值
print('键lover对应的值',dict1['lover'])
print(dict1['lover']+dict2['teacher'])
print(dict1,dict2)
# 修改字典
dict1['moment']='1996.12.11'   #更改moment键对应的值
dict1['时间']='2021.9.01'       #添加键值对，时间
print(dict1)
list1=[1,2,3]
dict1['hh']=list1             #添加键值对，hh值为列表
print(dict1)
tuple1=(1,2,3)
dict1['yy']=tuple1            #添加键值对，yy值为元组
print(dict1)
# 删除字典
# del dict1['时间']              #删除字典键是时间的键值对
# print(dict1)
# dict1.clear()                 #清空字典所有条目
# print(dict1)
# del dict1                   #删除字典
# print(dict1)

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