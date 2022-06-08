import re
import requests
import json


# 提取源码html响应文本标签字段：标题
headers = {
  'Connection': 'keep-alive',
  'Pragma': 'no-cache',
  'Cache-Control': 'no-cache',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Dest': 'document',
  'Referer': 'https://www.xbiquge.la/0/8/',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cookie': '_abcde_qweasd=0; UM_distinctid=17f87c92ffa202-03a7e03ecf8b35-977173c-1fa400-17f87c92ffba44; CNZZDATA1280571925=818030624-1647248712-https%253A%252F%252Fwww.baidu.com%252F%7C1647389112; Hm_lvt_8744b58bc1913cae0d8c4dc68f187d61=1647250584,1647395832; coupletAlllength=5; CNZZDATA1280571999=2089652069-1647240002-https%253A%252F%252Fwww.baidu.com%252F%7C1647389300; Hm_lvt_b48494e860b198c9c71009978cfc755e=1647250584,1647395832; fixedalllength=9; fixedall=8; Hm_lvt_169609146ffe5972484b0957bd1b46d6=1647250584,1647395832; Hm_lvt_2d2ceac9af7f7f1a8dbdd51db6dbf36c=1647250584,1647395832; Hm_lpvt_2d2ceac9af7f7f1a8dbdd51db6dbf36c=1647395832; 5531_2563_42.193.38.79=1; CNZZDATA1280572003=1441055998-1647250141-https%253A%252F%252Fwww.baidu.com%252F%7C1647389409; fixedall1length=8; CNZZDATA1280572006=1647809209-1647249081-https%253A%252F%252Fwww.baidu.com%252F%7C1647385096; Hm_lvt_dd3a5d36b1adfd567e4b8290c0760ba3=1647250584,1647395836; coupletAll=1_4; Hm_lpvt_b48494e860b198c9c71009978cfc755e=1647395839; richviews_5531=vOhLte13l%252Bqr1Dg9pwialFgXO0oo%252BUWe0mTz9cm%252BqsVH%252Fi4JXKDnJUMzLzn0Xvd3frL8%252BTyYD9H3KcUnZwOMkaM10QHI2bqs9h7TUUNgOWxPgwTpvzcpXtihDndbWKLjtwyl18Iz7RLvkPltiWuZlFJHPRe9EwmCJ0%252FrW6WuJtlp7GRmEjpLP9EqCg7tHwnJeAMFmBG4fmosow%252F0CcGrljAfKuab%252FfyXKjD1KWPl%252FrdWiBCJ76SpUYvwZkIF83G%252Bm20YF%252BtvI8h7HqlgAkOsdFocc2%252BPAsjgBFi5uChE00dL0r4r%252Bz3qTN7Ysb6AreGWVHa7PBzF0Xv3%252BWLMIhdoog%253D%253D; 5531_2334_42.193.38.79=1; Hm_lpvt_8744b58bc1913cae0d8c4dc68f187d61=1647395839; img3002500length=6; img3002500=0; Hm_lpvt_169609146ffe5972484b0957bd1b46d6=1647395839; CNZZDATA1280572013=220094920-1647240222-https%253A%252F%252Fwww.xbiquge.la%252F%7C1647391422; Hm_lvt_4ad6b1a6d9755b262a181c469db16477=1647250588,1647395839; Hm_lpvt_4ad6b1a6d9755b262a181c469db16477=1647395839; fixedall1=0_5; Hm_lpvt_dd3a5d36b1adfd567e4b8290c0760ba3=1647395840'
}
url='https://www.xbiquge.la/0/8/5599.html'
responese=requests.get(url=url,headers=headers)
# print(responese.text)
if responese.status_code==200:
    responese.encoding='utf-8'
    html=responese.text
    pattern1=re.compile(r'<title>(.*)</title>')
    title1=re.findall(pattern1,html)[0]
    pattern2 = re.compile(r'<meta name="description" content="(.+)" />')
    title2=re.findall(pattern2,html)[0]
    print(title1)
    print(title2)
# <title>大主宰_正文 第一章 北灵院_玄幻小说_新笔趣阁</title>
# <meta name="description" content="新笔趣阁提供了天蚕土豆创作的玄幻小说《大主宰》干净清爽无错字的文字章节：正文 第一章 北灵院在线阅读。" />



# 爬取图片数据
import os
from bs4 import BeautifulSoup
import requests
import re
import time



# tset_file = 'D:\Photo\get_image'
# bool = os.path.exists(tset_file)
# if bool == False:
#     os.mkdir('D:\Photo\kyouxi')
# header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
#             'cookie':'__yjs_duid=1_d2b85333a78251ee12b4979b497dcea91640681270600; Hm_lvt_14b14198b6e26157b7eba06b390ab763=1640681271; Hm_lvt_526caf4e20c21f06a4e9209712d6a20e=1640750282; zkhanecookieclassrecord=%2C66%2C54%2C55%2C; yjs_js_security_passport=8c280bad977ed7a39a302f2d311615dde82d18b2_1640769460_js; Hm_lpvt_526caf4e20c21f06a4e9209712d6a20e=1640769597'
#             }
# for item in range(2,116):
#     url = "https://pic.netbian.com/4kyouxi/index_{}.html".format(item)
#     response = requests.request("get", url,headers=header,).content
#     time.sleep(2)
#     soup=BeautifulSoup(response,'html.parser')
#
#     tag=soup.find_all('a')
#     for herf in soup.find_all('a'):
#         tes = str(herf.get('href'))
#         p1 = r"/tupian/.*?.html"
#         pattern1 = re.compile(p1)
#         # print(pattern1.findall(tes))
#         if len(pattern1.findall(tes))!=0:
#             path = pattern1.findall(tes)[0]
#             url_path = 'https://pic.netbian.com'+path
#             response = requests.request("get", url_path,headers=header).content
#             soup = BeautifulSoup(response, 'html.parser')
#             pic_path  = r'src="(.*?.jpg)'
#             pattern_path = re.compile(pic_path)
#             path_pic = pattern_path.findall(str(soup.find_all('a',id='img')))[0]
#             pic_path = 'https://pic.netbian.com'+path_pic
#             print(pic_path)
#             res = requests.request('get',pic_path,headers=header)
#             title =soup.find_all('a',id='img')
#             pic_re = r'title="(.*)"/></a>]'
#             pattern2 = re.compile(pic_re)
#             pic_title = pattern2.findall(str(soup.find_all('a',id='img')))[0]
#             print(pic_title)
#             try:
#                 with open(r'{}/{}.jpg'.format(tset_file,pic_title), 'wb') as f:
#                     print('开始下载图片')
#                     f.write(res.content)
#             except(OSError)as e:
#                 print(e)


