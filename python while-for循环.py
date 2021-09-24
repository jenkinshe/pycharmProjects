#python循环语句
#python while循环语句

a = 2  #while循环输出2-6的整数
while a < 6:
    print(a,'继续执行循环语句')
    a += 1
print(a, '循环结束')

var = 1

#continue、break跳过循环
i = 1
while i < 9:
    i += 1
    if i %2 > 0:
        continue   #跳出循环
    print(i)   #输出双数 2、4、6、8

i = 1
while 1:            # 循环条件为1必定成立
    print(i)         # 输出1~10
    i += 1
    if i > 10:     # 当i大于10时跳出循环
        break

#while循环 while...else...
y = 1
while y < 6:
    print(y,'小于6')
    y +=1
else:
    print(y,'大于6')

#无限循环
# count = 1
# while count:print('我喜欢燕燕')   #后面可以在同一行输出print

#python while_for循环
#for循环
i = '生活很难也要坚强'
a=[]
for a in i:
    print(a)
print('baibai')

fruits = ['banana','apple','mango','shiliu']
for fruit in fruits:
    print('当前水果是：',fruit)
print('没有水果了')

yy=[1,2,3,4,5,6,7,8,9]
for a in yy:
    print('字母是：',a)

#通过序列索引迭代  内置函数 len() 和 range(),函数 len() 返回列表的长度，即元素的个数。 range返回一个序列的数。
fruits=['bannan','apple','mango','shiliu']
print(len(fruits))
for index in range(len(fruits)):
    print('当前水果是：',fruits[index])
print('水果卖完了')

yy=[1,2,3,4,5,6,7,8,9]
for index in range(len(yy)):
    print('字母是：', yy[index])


#python循环嵌套
i = 2
while i < 100:
    j = 2
    while (j <= (i / j)):
        if not (i % j): break
        j = j + 1
    if (j > i / j): print(i, " 是素数")
    i = i + 1
print("Good bye!")


