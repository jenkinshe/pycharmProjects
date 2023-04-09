import json
import os,sys

sys.path.append(os.getcwd())
from testApi.common.get_cookie import get_cookie
import requests
import unittest
# import pytest
class Testxiaoxi(unittest.TestCase):
    def test_login(self):
        '检查登录是否成功'
        url_post = 'https://hrmstest.ovivas.cn/Home/Login'
        headers_post = {'content-type': 'application/json; charset=UTF-8'}
        data_post = {'account': 'sg8008', 'password': '11111a'}
        response_post = requests.post(url=url_post, headers=headers_post, data=json.dumps(data_post))
        print(response_post.json()['status'])
        self.assertEqual(response_post.json()['status'],'S100')

    def test_xiaoxi_01(self):
        '检查进入更多消息页面刷新数据是否正确'
        # a = get_cookie()
        # print(a)
        url_post_1 = 'https://hrmstest.ovivas.cn/Person/GetMessageList'
        headers_post_1 = {'content-type': 'application/json; charset=UTF-8', 'cookie':get_cookie()}
        data_post_1 = {'Status': 999, 'PageIndex': 1, 'PageSize': 10}
        response_post_1 = requests.post(url_post_1, headers=headers_post_1, data=json.dumps(data_post_1))
        result_expect = response_post_1.json()['data']['rows'][0]['messageTitle']
        print(result_expect)
        if result_expect in '2023年10月工资开始确认，请于2023-02-18 00:00:00前处理！':
            print('assertion is pass')
        else:
            print('assertion is false')
            self.assertEqual('2023年10月工资开始确认，请于2023-02-18 00:00:00前处理！',result_expect)
    def test_chaxun_01(self):
        '检查进入组织架构查询数据内容是否正确'
        url='https://hrmstest.ovivas.cn/Employees/GetEmployeesList'
        headers_post={'content-type': 'application/json; charset=UTF-8','cookie':get_cookie()}
        data_post={'userName':'', 'Organization':'', 'WorkStatus': ['0', '1', '2', '4', '5'], 'PostGradeId': 0}
        requests.post(url,headers=headers_post,data=json.dumps(data_post))
        result_post=requests.post(url, headers=headers_post, data=json.dumps(data_post))
        result_expect=result_post.json()['data']['model'][1]['name']
        print(result_expect)
        self.assertEqual(result_expect,'高山')
        self.assertIn(result_expect,'高山1')
    def test_chaxun_02(self):
        url='https://hrmstest.ovivas.cn/Employees/GetEmployeesList'
        headers_post={'content-type': 'application/json; charset=UTF-8','cookie':get_cookie()}
        data_post={'userName': 'sg2323', 'Organization': '', 'WorkStatus': ['0', '1', '2', '4', '5'], 'PostGradeId': 0}
        result_post=requests.post(url,headers=headers_post,data=json.dumps(data_post))
        result_expect_01=result_post.json()['data']['model'][0]['picture']
        result_expect_02=result_post.json()['data']['model'][0]['jobnumber']
        result_expect_03=result_post.json()['data']['model'][0]
        self.assertEqual(result_expect_01,'/Upload/UserPicture/20221228155732338148632.jpg')
        self.assertIn('SG2323',result_expect_02)
        self.assertIn("userId",result_expect_03)
    def test_chaxun_03(self):
        url='https://hrmstest.ovivas.cn/Performance/GetQuarterManage'
        headers_post={'content-type': 'application/json; charset=UTF-8','cookie':get_cookie()}
        data_post={'Id': 20, 'Depart': '', 'Name': '', 'Score': '999', 'PostId': '', 'QuarterType': 2}
        result_post = requests.post(url, headers=headers_post, data=json.dumps(data_post))
        result_expect=result_post.json()['data']['isCheckEndTime']
        print(result_expect)
        self.assertEqual(result_expect,1)


if __name__ == '__main__':
    unittest.main()
# if __name__ == '__main__':
#     pytest.main()

