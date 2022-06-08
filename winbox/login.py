import requests
import json
import os
import base64
import re
# 登录winbox后台获取token

def login_token(username,password):
    '获取登录接口中返回的token'
    url = 'https://wbx3-master.ovivas.cn/Token/CreateToken'
    headers = {
        'authority': 'wbx3-master.ovivas.cn',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'accept': '*/*',
        'content-type': 'application/json; charset=UTF-8',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://wbx3-agent.ovivas.cn',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://wbx3-agent.ovivas.cn/',
        'accept-language': 'zh-CN,zh;q=0.9',
    }
    request_payload = {'Username': username, 'Password': password, 'ClientType': "Web"}
    response = requests.post(url, headers=headers, data=json.dumps(request_payload))
    print(response.json()['data']['token'])

# login_token("APCOMPANY2","11111a")
token_1=login_token("APCOMPANY2","11111a")


def smslogin_token():
    '获取验证码网址登录token'
    url = "https://masterapi-wbx.ovivas.cn/Token/CreateToken"
    requests_payload = {"Username":"ADMINSUB12","Password":"11111a","ClientType":"Web"}
    headers = {
        'origin': 'https://agent-wbx.ovivas.cn',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36',
        'content-type': 'application/json; charset=UTF-8',
        'accept': '*/*',
        'referer': 'https://agent-wbx.ovivas.cn/Account/Login',
        'authority': 'masterapi-wbx.ovivas.cn'
    }
    response = requests.post(url, headers=headers, data=json.dumps(requests_payload))
    print(response.json()['data']['token'])
# smslogin_token()
token_2=smslogin_token()



def sendsms():
    '发送验证码'
    try:
        url = 'https://wbx3-master.ovivas.cn/MasterAPI/Special/AuthSendSms'
        headers = {
            'authority': 'wbx3-master.ovivas.cn',
            'pragma': 'no-cache',
            'cache-control': 'no-cache',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'content-type': 'application/json;charset=UTF-8',
            'authorization': 'Bearer %s'%(token_1),
            'sec-ch-ua-mobile': '?0',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
            'sec-ch-ua-platform': '"Windows"',
            'origin': 'https://wbx3-agent.ovivas.cn',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://wbx3-agent.ovivas.cn/',
            'accept-language': 'zh-CN,zh;q=0.9'
        }
        requests_payload = {"SendType": 10, "UserId": "", "PhoneNo": ""}
        response = requests.post(url, headers=headers, data=json.dumps(requests_payload))
        print(response.text)
    except:
        print('失败')
sendsms()



def smslist():
    '查询验证码'
    try:
        url = 'https://masterapi-wbx.ovivas.cn/MasterAPI/User/GetSmsList'
        headers = {
            'origin': 'https://agent-wbx.ovivas.cn',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'authorization': 'Bearer %s' %(token_2),
            'content-type': 'application/json;charset=UTF-8',
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'referer': 'https://agent-wbx.ovivas.cn/',
            'authority': 'masterapi-wbx.ovivas.cn',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36'
        }

        requests_payload = {"UserId": "602364525"}
        response = requests.post(url, headers=headers, data=json.dumps(requests_payload))
        print(response)
        print(response.text)
    except:
        print('失败')
smslist()



# def verifysms():
#     '验证验证码'
#     url = 'https://wbx3-master.ovivas.cn/MasterAPI/Auth/VerifyLoginSms'
#     headers={
#         'authority': 'wbx3-master.ovivas.cn',
#         'pragma': 'no-cache',
#         'cache-control': 'no-cache',
#         'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
#         'accept': 'application/json, text/javascript, */*; q=0.01',
#         'content-type': 'application/json;charset=UTF-8',
#         'authorization': 'Bearer %s' % (token_1),
#         'sec-ch-ua-mobile': '?0',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
#         'sec-ch-ua-platform': '"Windows"',
#         'origin': 'https://wbx3-agent.ovivas.cn',
#         'sec-fetch-site': 'same-site',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-dest': 'empty',
#         'referer': 'https://wbx3-agent.ovivas.cn/',
#         'accept-language': 'zh-CN,zh;q=0.9'
#     }
#     requests_payload = {"SmsCode": }
#     response=requests.post(url,headers=headers,data=json.dumps(requests_payload))
#     print(response.text)
# verifysms()

# def transfer(PAYER,RECER,N):
#     '转账'
#     try:
#         url = 'https://wbx3-master.ovivas.cn/MasterAPI/Wallet/GenerationTransfer'
#         headers = \
#             {
#                 'authority': 'wbx3-master.ovivas.cn',
#                 'pragma': 'no-cache',
#                 'cache-control': 'no-cache',
#                 'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
#                 'accept': 'application/json, text/javascript, */*; q=0.01',
#                 'content-type': 'application/json;charset=UTF-8',
#                 'authorization': 'Bearer %s'%(token_1),
#                 'sec-ch-ua-mobile': '?0',
#                 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
#                 'sec-ch-ua-platform': '"Windows"',
#                 'origin': 'https://wbx3-agent.ovivas.cn',
#                 'sec-fetch-site': 'same-site',
#                 'sec-fetch-mode': 'cors',
#                 'sec-fetch-dest': 'empty',
#                 'referer': 'https://wbx3-agent.ovivas.cn/',
#                 'accept-language': 'zh-CN,zh;q=0.9'
#             }
#         requests_payload = {"PaymentPerson": PAYER, "ReceiverPerson": RECER, "Amount": N}
#         response = requests.post(url, headers=headers, data=json.dumps(requests_payload))
#         print(response.text)
#     except:
#         print('失败')
# transfer('APCOMPANY2','WBPWANJIAJ09298228',2)








