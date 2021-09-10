i=10
print(i)
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
driver.find_element_by_id('kw').click()
driver.find_element_by_id('kw').send_keys('奥运会')
# driver.find_element_by_xpath('//*[@id="su"]').click()
driver.find_element_by_id('kw').send_keys('直播')
driver.find_element_by_id('su').click()
name=driver.find_element_by_id('kw')
