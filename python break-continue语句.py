i = 1
print(i)
#break语句   跳出整个循环
yy = ['yy','bobo','cc','love']
for letter in yy:
    if letter == 'love':   #for循环，遍历执行到love跳出循环
        break
    print(letter)
print('bye bye')

yy = ['like','love','yy','bobo']
for index in range(len(yy)):
    if yy[index] == 'yy':    #for循环，通过序列索引迭代，遍历到yy时跳出循环
        break
    print(yy[index])
print('再见')

a = 1
while a < 6:
    print('这个值为：',a)
    a += 1
    if a == 4:  #while循环，a等于4跳出循环
        print(a)
        break

yy = 'yifanfengshun'
for index in range(len(yy)):
    if yy[index] == 'f':    #for循环，通过序列索引迭代，遍历到yy时跳出循环
        break               #跳出整个循环
    print(yy[index])
print('再见')

#continue语句   跳出本次循环
fruits = ['banana','apple','mango','liulian']
for fruit in fruits:
    if fruit == 'mango':    #遍历到mango，跳出本次循环
        continue            #跳出本次循环
    print(fruit)
print('除了mango没有，其他水果都有')

students = ['yy','bobo','mm','leilei']
for index in range(len(students)):
    if students[index] == 'mm':    #遍历到mm，continue跳出本次循环
        continue                   #跳出本次循环
    print(students[index])
print('除了mm没到，其他同学都到位了')

var = 10
while var > 0:
    var -= 1
    if var == 6:       #遍历到var等于6，continue跳出本次循环
        continue       #跳出本次循环
    print('当前变量值：',var)
print('good bye')

#输出0-10的奇数
a = 10
while a > 0:
    a -=1
    if a %2==0:     #符合偶数条件，continue跳出本次循环
        continue    #跳出本次循环
    else:
        print('当前值为奇数odd：',a)

#pass语句
a = 'python'
for letter in a:
    if letter =='h':
        pass   #空语句，保证程序结构完整性，不做任何事情
        print('难受')
    print('当前字符为：', letter)

def function():
    pass      #pass用于占位置，python 3.0可以不用写，可写可不写





