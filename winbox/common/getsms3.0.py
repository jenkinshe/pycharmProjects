# -*- coding: utf-8 -*-
# @Time : 2021/12/10 12:30
# @Author : hh
# @File : getsms3.0.py


import requests
import json
import re
phone='60123456'
class GET_SMS_3:
    def GET_TOKEN_2(self):
        try:
            url = 'https://masterapi-wbx.ovivas.cn/Token/CreateToken'
            headers ={
                'content-type': 'application/json; charset=UTF-8',
                'origin': 'https://agent-wbx.ovivas.cn'
            }
            requests_payload={"Username":"ADMINSUB12","Password":"11111a","ClientType":"Web"}
            response=requests.post(url,headers=headers,data=json.dumps(requests_payload))
            TOKEN_2=response.json()['data']['token']
            # print(type(response.json()['data']))
            # print(TOKEN_2)
            return TOKEN_2
        except Exception as e:
            print('登录失败！')
            raise e
    def getsms_2(self,TOKEN_2):
        try:
            url = 'https://masterapi-wbx.ovivas.cn/MasterAPI/User/GetSmsList'
            payload = f"{{'UserId':'{phone}'}}"
            headers = {
                    'authorization': 'Bearer %s' %(TOKEN_2),
                    'content-type': 'application/json;charset=UTF-8',
                }
            response = requests.request('POST', url, headers=headers, data=payload)
            res = json.loads(response.text)
            if len(res['data']) == 0:
                print(f'未找到电话:{phone} 的验证码...')
            else:
                sms_content = res['data'][0]['content']
                Sms = re.findall(r'\d{6}', sms_content)[0]
                # print(f'{phone} 的短信验证码为：{Sms}')
                # print(Sms)
                return Sms

            # print(type(res['data']))
            # if len(res['data']) < 10:
            #     for i in res['data']:
            #         print(i['smsTo'],i['content'])
            # else:
            #     for i in res['data'][0:10]:
            #         print(i['smsTo'], i['content'])
            # print("\n")
        except Exception as e:
            print('登录超时,重新打开.')
            raise e

    def GET_TOKEN_3(self):
        try:
            url ='https://wbx3-master.ovivas.cn/Token/CreateToken'
            headers = {
                'content-type': 'application/json; charset=UTF-8',
                'origin': 'https://wbx3-agent.ovivas.cn'
            }
            requests_payload={"Username":"adminsub33","Password":"123456a","ClientType":"Web"}
            response=requests.post(url,headers=headers,data=json.dumps(requests_payload))
            TOKEN_3=response.json()['data']['token']
            # print(TOKEN_3)
            return TOKEN_3
        except Exception as e:
            print('登录失败！')
            raise e

    def sendsms_3(self,TOKEN_3):
        try:
            url = "https://wbx3-master.ovivas.cn/MasterAPI/Special/AuthSendSms"

            requests_payload = {"SendType":10,"UserId":"","PhoneNo":""}
            headers = {
                'origin': 'https://wbx3-agent.ovivas.cn',
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'zh-CN,zh;q=0.9',
                'authorization': 'Bearer %s'%(TOKEN_3),
                'content-type': 'application/json;charset=UTF-8',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'referer': 'https://wbx3-agent.ovivas.cn/Account/AuthLogin',
                'authority': 'wbx3-master.ovivas.cn',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36'
            }
            response = requests.request("POST", url, headers=headers, data=json.dumps(requests_payload))
            # print(requests_payload)
            # print('响应成功',response.text)
        except Exception as e:
            print('登录失败！')
            raise e

    def verifysms_3(self,sms,TOKEN_3):
        try:
            url = "https://wbx3-master.ovivas.cn/MasterAPI/Auth/VerifyLoginSms"
            requests_payload = f"{{'SmsCode':'{sms}'}}"
            headers = {
                'authorization': 'Bearer %s'%(TOKEN_3),
                'content-type': 'application/json;charset=UTF-8',
            }
            response = requests.request('POST', url, headers=headers, data=requests_payload)
            # print(type(response.text),response.text)
        except Exception as e:
            print('登录失败！')
            raise e
    def getsms_3(self,TOKEN_3):
        try:
            url = 'https://wbx3-master.ovivas.cn/MasterAPI/User/GetSmsList'
            payload = "{'UserId':''}"
            headers = {

                'authorization': 'Bearer %s' % (TOKEN_3),
                'content-type': 'application/json;charset=UTF-8',
            }
            response = requests.post(url, headers=headers, data=payload)
            res = json.loads(response.text)
            # print(res,type(res))
            if len(res['data']) < 10:
                for i in res['data']:
                    print(i['smsTo'],i['content'])
            else:
                for i in res['data'][0:10]:
                    print(i['smsTo'], i['content'])
            # print("\n")
        except Exception as e:
            print('登录超时,重新打开.')
            raise e

if __name__ == '__main__':
    def SMS3():
        w = GET_SMS_3()
        TOKEN_3 = w.GET_TOKEN_3()
        TOKEN_2 = w.GET_TOKEN_2()
        w.sendsms_3(TOKEN_3)
        sms = w.getsms_2(TOKEN_2)
        w.verifysms_3(sms,TOKEN_3)
        w.getsms_3(TOKEN_3)
    while True:
        input("键入回车获取最新验证码：")
        SMS3()
        print('--------$$$-------\n')
















