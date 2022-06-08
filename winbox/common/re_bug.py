import os
from bs4 import BeautifulSoup
import requests
import re
import time



tset_file = 'D:\Photo'
bool = os.path.exists(tset_file)
if bool == False:
    os.mkdir('D:\Photo')
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
            'cookie':'__yjs_duid=1_d2b85333a78251ee12b4979b497dcea91640681270600; Hm_lvt_14b14198b6e26157b7eba06b390ab763=1640681271; Hm_lvt_526caf4e20c21f06a4e9209712d6a20e=1640750282; zkhanecookieclassrecord=%2C66%2C54%2C55%2C; yjs_js_security_passport=8c280bad977ed7a39a302f2d311615dde82d18b2_1640769460_js; Hm_lpvt_526caf4e20c21f06a4e9209712d6a20e=1640769597'
            }
for item in range(2,10):
    url = "https://pic.netbian.com/4kmeinv/index_{}.html".format(item)
    response = requests.request("get", url,headers=header,).content
    time.sleep(2)
    soup=BeautifulSoup(response,'html.parser')

    tag=soup.find_all('a')
    for herf in soup.find_all('a'):
        tes = str(herf.get('href'))
        p1 = r"/tupian/.*?.html"
        pattern1 = re.compile(p1)
        # print(pattern1.findall(tes))
        if len(pattern1.findall(tes))!=0:
            path = pattern1.findall(tes)[0]
            url_path = 'https://pic.netbian.com'+path
            response = requests.request("get", url_path,headers=header).content
            soup = BeautifulSoup(response, 'html.parser')
            pic_path  = r'src="(.*?.jpg)'
            pattern_path = re.compile(pic_path)
            path_pic = pattern_path.findall(str(soup.find_all('a',id='img')))[0]
            pic_path = 'https://pic.netbian.com'+path_pic
            print(pic_path)
            res = requests.request('get',pic_path,headers=header)
            title =soup.find_all('a',id='img')
            pic_re = r'title="(.*)"/></a>]'
            pattern2 = re.compile(pic_re)
            pic_title = pattern2.findall(str(soup.find_all('a',id='img')))[0]
            print(pic_title)
            try:
                with open(r'{}/{}.jpg'.format(tset_file,pic_title), 'wb') as f:
                    print('开始下载图片')
                    f.write(res.content)
            except(OSError)as e:
                print(e)