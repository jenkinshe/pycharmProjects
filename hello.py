# f=open('cee.txt','x')
import os

f=open('cee.txt','w')   #创建文件cee.txt
f.write('i love you')   #写入内容
f=open('cee.txt','r')   #打开cee.txt文件，阅读
print(f.read())         #open返回对象赋值给f，阅读
f=open('cee.txt','a')   #给文件cee.txt追加内容，赋值给f
f.write('新增加的内容1')  #写入内容
f=open('cee.txt','r')   #打开cee.txt文件，阅读
print(f.read())        #open返回对象赋值给f，阅读前三个

# os.remove('cee.txt')    #删除文件cee.txt
#判断cee.txt文件是否存在，存在即删除，不存在则打印内容
# if os.path.exists('cee.txt'):
#     os.remove('cee.txt')
# else:
#     print('"cee.txt"文件不存在')
# os.rmdir('文件') #提示：只能删除空文件夹