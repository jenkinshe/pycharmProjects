import json

import requests

def get_cookie():
    '登录后从响应头获取cookie'
    url_post = 'https://hrmstest.ovivas.cn/Home/Login'
    headers_post = {'content-type': 'application/json; charset=UTF-8'}
    data_post = {'account': 'sg8008', 'password': '11111a'}
    response_post = requests.post(url=url_post, headers=headers_post, data=json.dumps(data_post))
    # print(response_post.headers)
    # print(response_post.json())
    # print(response_post.url)
    # print(response_post.status_code)
    # print(response_post.headers['Set-Cookie'])
    # print(response_post.cookies)
    cok = response_post.headers['Set-Cookie']
    cokie=cok.split(';')[0]
    # print(cokie)
    # a_cookie = requests.utils.dict_from_cookiejar(response_post.cookies)
    # print(a_cookie)
    # headers_common={'cookie':'.AspNetCore.Cookies='+a_cookie['.AspNetCore.Cookies']}
    # print(cok)
    return cokie
# a=get_cookie()
# print(a)
