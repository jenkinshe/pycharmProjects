# python列表
list1 = ['youchengyan','heqing','yy','bobo',1211,222]
list2 = ['YCY','HQ',1996,1998]
list3 = ['2021.6.24','2021.9.1']
# 访问列表中的值
print(list1[4],list1[5],list2[0:2],list3[0])
print(list3[:])

#更改列表值，赋值
list4 = ['aa','bb','cc','dd']
list4[1] = 'yy'       #赋值，给索引下标为1的元素赋值更改为yy
print('list4列表：',list4)
#新增列表元素append
list4.append('heqing')    #新增元素在列表，append，新增
print('在list4列表末尾新增heqing元素后列表：',list4)
# 删除列表元素del
del list4[0]             #删除列表索引下标为0的元素
print('删除list4列表下标为0的元素后列表：',list4)
# del list4                #删除整张列表list4
# print(list4[:])

#python列表脚本操作符
print(len([1,2,3]))
print(list1+list2)
print(list1*2)
print('youchengyan' in list1)
print(list1 is list1)
for a in list1:
    print('遍历list1列表元素：',a)

# Python列表函数&方法
# 函数len、max、min、cmp
print(len([3,5,6]))    #输出列表元素长度
print(max([6,9,18]))   #输出列表中元素最大值
print(min(6,9,7))      #输出元组中元素最小值
tuple_1 = (6,9,8)      #元组tuple_1
print(list(tuple_1))   #输出将元组tuple_1转变为列表
list5 = [6,9,3,6,9,2]  #列表list5
print(tuple(list5))    #输出将列表list5转变为元组

#方法  append、extend、pop、remove、reverse、sort、count、index
list6 = ['燕燕','啵啵']
# append添加
list6.append([2,9])    #在列表添加新的对象列表
print(list6[2][0])     #输出列表中的列表元素
print(list6)
list6.append('love')   #在列表末添加新的对象
print(list6)
# extend追加
list6.extend([2,6,'miss'])  #在列表末尾一次性追加另一个序列中的多个值
print(list6)
list6.extend(list5)        #在列表末尾追加另一个列表
print(list6)
list6.extend('tongshi')     #若追加的事字符串，那么每一个字符都会分别追加到末尾
print(list6)
# coun统计元素出现次数
print(list6.count('t'))    #输出t元素字符出现在列表中的次数
# Index找出某个值第一次出现的索引位置
print(list6.index('o'))    #从列表中找出某个值的第一个匹配的索引位置
# list6.insert()
# print(list6)
# pop移除列表中某一个元素
list6.pop()         #移除列表中默认最后元素
print(list6)
print(list6.pop())  #移除列表中最后一位元素并返回该元素的值（返回被移除末尾的元素值）
print(list6)
# remove移除列表中某个值的第一个匹配项
list6.remove('love')  #移除列表中元素love值
print(list6)
# reverse反向展示列表中的元素
list6.reverse()      #反向展示列表元素
print(list6)
# print(list6[2:6])
# sort对列表进行排序,默认展示升序
list7 = [1,2,3,4,9,8,5,6,9,8,2,5,2]
list7.sort()          #对列表元素进行升序展示
print(list7)



#两表的追加
list8 = ["a", "b" , "c"]
list9 = [1, 2, 3]
for x in list9:     #遍历list9
    list8.append(x) #将遍历中的值依次添加到list8中
print(list8)
#若列表中无元素则加到列表中
list10=['fruit','banana','apple']
if 'orange' in list10:
    print('"orange"在列表10中')
else:
    list10.append('orange')
print(list10)
#判断列表中元素是否在另一列表中，若不在另一列表则依次加到另一列表中
list11=['fruit','banana','apple','pandan']
list12=['fruit','apple','club','winboxth']
for a in list11:
    if a in list12:
        print(a,'已经在列表list12中了')
    else:
        list12.append(a)
print(list12)


#遍历列表 for循环对列表中元素依次遍历打印
#添加append、extend、insert
#删除remove、pop、del
#清空列表元素clear
#复制列表copy()、list()
#合并列表 +、遍历追加append、extend列表
#list构造函数
type1=("apple", "banana", "cherry")
list12=list(type1)     #将元组更改为列表类型
print(list12)
list13=list(("apple12", "banana12", "cherry65"))  #等同于直接把元组放在列表中
print('list13为：',list13)
