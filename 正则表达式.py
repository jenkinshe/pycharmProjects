# 正则表达式
import re
rehe='he52455kjkk'
matchobject=re.match(r'(.*)245(.*)',rehe,flags=0)
if matchobject:
    print('matchobject.group():',matchobject.group())
    print('matchobject.group(1):',matchobject.group(1))
    print('matchobject.group(2):',matchobject.group(2))
    print('matchobject.groups():',matchobject.groups())
else:
    print('no match!')


# 1.re.match() 与 re.search()区别
# re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配（注意：仅仅是第一个）
rediff='fd25hGJKj41g52'
match_object_1=re.match(r'25hG',rediff)
print("match_object_1:",match_object_1)
search_object_1=re.search(r'25hG',rediff)
print('search_object_1:',search_object_1)

# 2.re.findall()
# 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表
findall_object_1=re.findall(r'\d{3}','hgf552lll58lll987jjj8')   #\d{3}若有3个连续数字则匹配；re.findall()匹配所有符合条件的字符
print('findall_object_1:',findall_object_1)
for a in findall_object_1:
    print(a)
else:
    print('for循环遍历结束')

# 3.re.finditer()
#和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回
#re.finditer(pattern, string, flags=0)
finditer_object_1=re.finditer(r'\d+','hgf552lll58lll987jjj8')
for a in finditer_object_1:
    print(a.group())


# 3.re.split()分隔；把字符分割为一个列表并返回成功匹配的列表
rsplit=re.split(r'\.|\^','dgk^f^^g.gd2ff2g')   #用.或^作为分隔符分隔字符串
print('分割出的列表rsplit:',rsplit)

# 4.re.sub()替换；用于替换字符串中的匹配项
# 语法：re.sub(pattren,repl,string,count=0)
rsub=re.sub(r'hh','bobo','yy want to be hh with together  hh is  one hh',count=2)  #将pattern替换为repl；将hh替换为bobo,替换两次
print('替换后的字符串rsub:',rsub)

# 5.re.compile()编译；compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，然后就可以用编译后的正则表达式去匹配字符串
test_pattern_1=re.compile(r'\d{3}')    #编译一个开头匹配3位连续数字的正则表达式
test_match=test_pattern_1.match('1258gf54512')   #匹配字符串
print(test_match)                   #匹配出结果
# print(test_pattern_1.match('1258gf54512'))
print(re.findall(test_pattern_1,'1258gf54512'))




# 正则表达式实战
# 1.清除手机号码
s = ('13115021381','18277122391','17823912311','20218231923','138291229811') ## 输出手机号码的数据，其中第4个数据不是手机号码（开头不是1）、第5个数据不是手机号码（有12位）
pattern_1=r'[1][26897]\d{9}$'     ## 设置正则化匹配的模式，手机号码是11位，第1位是1，第2为是26897中的一个，然后剩下9位数，用\d{9}来完成，最后用$表示结尾（即只匹配11个数）
a=[]
for data_1 in s:
    if re.findall(pattern_1,data_1)!=[]:
        a.append(data_1)
print(a)
# 2.清除座机号码
s= ['010-28172132','0231-3817212','031-42312772','023-498281211','0131-39897123','0102321231']
pattern_2=r'\d{2,3}-\d{7,8}$'    ## 座机号码的格式2或3数字-7或8数字,最后用$表示结尾（即只匹配11个数）
b=[]
for data_2 in s:
    if re.findall(pattern_2,data_2)!=[]:
        b.append(data_2)
print(b)

# 3、提取数据中出现“h”和“好”的数据，不区分大小写re.I
s = ['Hi','好','human','真好吃']     # 设置模拟的数据
pattern_3=r'h'                     #编译正则表达式pattern
pattern_4=r'好'
a1=[]                              #设置两个空列表存储数据
a2=[]
for data_3 in s:                   #for循环遍历列表s
    if re.findall(pattern_3,data_3,re.I) !=[]:   #re.findall()返回列表.若未匹配上返回空列表
        a1.append(data_3)                        #将匹配上的data_3存放在空列表a1中
print('数据中出现“h”,a1:',a1)
for data_4 in s:
    if re.findall(pattern_4,data_4,re.I)!=[]:    #将需要拿来匹配的正则pattern_4与data_4进行匹配，若匹配上了
        a2.append(data_4)                         #将匹配上的data_4存放在空列表a2中
print('数据中出现“好”,a2:',a2)

# 4、提取数据集中包含“H2O”的数据
s = ['H2O','水H2O','过氧化氢H2O2','氢气H2']     # 设置模拟的数据
pattern_5=r'\w*h2o'                       # 设置pattern的格式，在H2O的前后添加\w，然后使用*来表示查找任意数量的数据
a3=[]
for data_5 in s:
    if re.findall(pattern_5,data_5,re.I)!=[]:
        a3.append(data_5)
print('数据集中包含“H2O”的数据a3:',a3)


# 5、提取QQ邮箱
s = ['182872@qq.com','1232@qq.com','12342@qq.com.cn','sAnBe2am@qq.com','sWM@qq.com']    # 设置模拟的数据，其中第2个、第3个和第5个数据都不是需要提取的数据
pattern_6 = re.compile('[a-zA-Z0-9]{5,}@qq.com$' )  # 设置提取的规则，设定是5个字符及以上@qq.com，其他都不是正确的QQ邮箱，其中[a-zA-Z0-9]表示既可以是大小写字母，也可以是数字;[a-zA-Z0-9],匹配任何字母及数字
a4=[]
for data_6 in s:
    if re.findall(pattern_6,data_6)!=[]:
        a4.append(data_6)
print('是5个字符及以上@qq.com为：a4:',a4)



# 6.group(0)和groups（）
pattern_7=re.compile(r'\d+-\d{3,8}$')
s = ['6-45561','3-154','582-156','3-584']
a5=[]
for data_7 in s:
    if re.findall(pattern_7,data_7)!=[]:
        a5.append(data_7)
    print(a5)
else:
    print('no find')




# 模式	描述
# ^	匹配字符串的开头
# $	匹配字符串的末尾。
# .	匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
# [...]	用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
# [^...]	不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
# re*	匹配0个或多个的表达式。
# re+	匹配1个或多个的表达式。
# re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
# re{ n}	精确匹配 n 个前面表达式。例如， o{2} 不能匹配 "Bob" 中的 "o"，但是能匹配 "food" 中的两个 o。
# re{ n,}	匹配 n 个前面表达式。例如， o{2,} 不能匹配"Bob"中的"o"，但能匹配 "foooood"中的所有 o。"o{1,}" 等价于 "o+"。"o{0,}" 则等价于 "o*"。
# re{ n, m}	匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
# a| b	匹配a或b
# (re)	对正则表达式分组并记住匹配的文本
# (?imx)	正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
# (?-imx)	正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
# (?: re)	类似 (...), 但是不表示一个组
# (?imx: re)	在括号中使用i, m, 或 x 可选标志
# (?-imx: re)	在括号中不使用i, m, 或 x 可选标志
# (?#...)	注释.
# (?= re)	前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
# (?! re)	前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功
# (?> re)	匹配的独立模式，省去回溯。
# \w	匹配字母数字及下划线
# \W	匹配非字母数字及下划线
# \s	匹配任意空白字符，等价于 [ \t\n\r\f]。
# \S	匹配任意非空字符
# \d	匹配任意数字，等价于 [0-9].
# \D	匹配任意非数字
# \A	匹配字符串开始
# \Z	匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。
# \z	匹配字符串结束
# \G	匹配最后匹配完成的位置。
# \b	匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
# \B	匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
# \n, \t, 等.	匹配一个换行符。匹配一个制表符。等
# \1...\9	匹配第n个分组的内容。
# \10	匹配第n个分组的内容，如果它经匹配。否则指的是八进制字符码的表达式。

# 正则表达式实例
# 字符匹配
# 实例	描述
# python	匹配 "python".
# 字符类
# 实例	描述
# [Pp]ython	匹配 "Python" 或 "python"
# rub[ye]	匹配 "ruby" 或 "rube"
# [aeiou]	匹配中括号内的任意一个字母
# [0-9]	匹配任何数字。类似于 [0123456789]
# [a-z]	匹配任何小写字母
# [A-Z]	匹配任何大写字母
# [a-zA-Z0-9]	匹配任何字母及数字
# [^aeiou]	除了aeiou字母以外的所有字符
# [^0-9]	匹配除了数字外的字符
# 特殊字符类
# 实例	描述
# .	匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]' 的模式。
# \d	匹配一个数字字符。等价于 [0-9]。
# \D	匹配一个非数字字符。等价于 [^0-9]。
# \s	匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
# \S	匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
# \w	匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。
# \W	匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'。




