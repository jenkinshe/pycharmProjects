# -*- coding: utf-8 -*-
# @Time : 2020/11/02 11:02
# @Author : CC
# @File : test_mode.py
import requests,json,re

Protocol_header = "https"
Request_method = 'POST'
url = 'masterapi-wbx.ovivas.cn'
class WBX_SMS:
    def Get_Token(self):
        try:
            url_addr = f"{Protocol_header}://{url}/Token/CreateToken"
            payload = "{'Username':'adminsub2','Password':'11111a','ClientType':'Web'}"
            headers = {
                'content-type': 'application/json; charset=UTF-8',
                'origin': 'https://agent-wbx.ovivas.cn'
            }
            response = requests.request(Request_method, url=url_addr, headers=headers, data=payload)
            # print(response.text,type(response.text))
            token = json.loads(response.text)['data']['token']#获取token字段
            return token
            # while True:
            #     phone = input('请输入电话号码：')
            #     url_addr = f"{Protocol_header}://{url}/MasterAPI/User/GetSmsList"
            #     payload = "{\"UserId\":\"%s\"}" % phone
            #     headers = {
            #         'authorization': 'Bearer %s' % (token),
            #         'content-type': 'application/json;charset=UTF-8',
            #     }
            #     response = requests.request(Request_method, url=url_addr, headers=headers, data=payload)
            #     res = json.loads(response.text)
            #     if len(res['data']) == 0:
            #         print(f'未找到电话:{phone} 的验证码...')
            #     else:
            #         sms_content = res['data'][0]['content']
            #         Sms = re.findall(r'\d{6}', sms_content)[0]
            #         print(f'{phone} 的短信验证码为：{Sms}')
        except Exception as e:
            print('登录失败！')
            raise e


    def Get_Sms(self,token):
        try:
            url_addr = f"{Protocol_header}://{url}/MasterAPI/User/GetSmsList"
            payload = "{'UserId':' '}"
            headers = {
                    'authorization': 'Bearer %s' % (token),
                    'content-type': 'application/json;charset=UTF-8',
                }
            response = requests.request(Request_method, url=url_addr, headers=headers, data=payload)
            res = json.loads(response.text)
            # print(type(res['data']))
            if len(res['data']) < 10:
                for i in res['data']:
                    print(i['smsTo'],i['content'])
            else:
                for i in res['data'][0:10]:
                    print(i['smsTo'], i['content'])
            print("\n")
        except Exception as e:
            print('登录超时,重新打开.')
            raise e

if __name__ == '__main__':
    while True:
        input("键入回车获取最新验证码：")
        w = WBX_SMS()
        TOKEN = w.Get_Token()
        w.Get_Sms(TOKEN)
