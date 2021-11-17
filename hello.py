# i=10
# print(i)
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com/')
# driver.find_element_by_id('kw').click()
# driver.find_element_by_id('kw').send_keys('奥运会')
# # driver.find_element_by_xpath('//*[@id="su"]').click()
# driver.find_element_by_id('kw').send_keys('直播')
# driver.find_element_by_id('su').click()
# name=driver.find_element_by_id('kw')


import requests
import random
url='http://hrms.ovivas.cn/Employees/GetOrgNameList'
params={"account":"sg0102","password":"760402621HE"}
r=requests.post(url,params)
print(r.url)
print(r.json())