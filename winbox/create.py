import requests
import json
# from login import login_token
# # login_token("APCOMPANY2","11111a")


url= 'https://wbx3-master.ovivas.cn/MasterAPI/Wallet/GenerationTransfer'
headers=\
{
'authority':'wbx3-master.ovivas.cn',
'pragma':'no-cache',
'cache-control':'no-cache',
'sec-ch-ua':'"Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
'accept':'application/json, text/javascript, */*; q=0.01',
'content-type':'application/json;charset=UTF-8',
'authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoiQVBDT01QQU5ZMiIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvc2VyaWFsbnVtYmVyIjoiV2ViIiwiaHR0cDovL3NjaGVtYXMubWljcm9zb2Z0LmNvbS93cy8yMDA4LzA2L2lkZW50aXR5L2NsYWltcy9leHBpcmVkIjoiMTIvOS8yMDIxIDM6MDE6MTQgUE0iLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3VzZXJkYXRhIjoiODAxYmJiYWNmNGI4NDUxZGFiYjgzZjRjMWUzNGI2YzkyMDIxMTIwNjE1MDEiLCJleHAiOjE2MzkwMzMyNzQsImlzcyI6Imh0dHA6Ly8xMi5mYjg4Lm5ldC8iLCJhdWQiOiJodHRwOi8vMTIuZmI4OC5uZXQvIn0.1RxdyADiaFxnSpVgUHH5L4rGLCuBYgHzoJXcyODVQsk)',
'sec-ch-ua-mobile':'?0',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
'sec-ch-ua-platform':'"Windows"',
'origin':'https://wbx3-agent.ovivas.cn',
'sec-fetch-site':'same-site',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://wbx3-agent.ovivas.cn/',
'accept-language':'zh-CN,zh;q=0.9'
}
payload = {"PaymentPerson":"APCOMPANY2","ReceiverPerson":"WBPWANJIAJ09298228","Amount":"2"}
print(payload)
response = requests.post(url,headers=headers,data=json.dumps(payload))
print(response.json())





# a = 0
# for a in range(3):
#     create01()
#     a =a + 1
#     print('总数：'a)
