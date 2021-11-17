import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

driver=webdriver.Chrome()
driver.get('https://wbx3-agent.ovivas.cn/Account/Login#/Home')
s = driver.find_element_by_xpath('//select[@id="Language"]')    #实例化select
Select(s).select_by_value('zh-CN')    #select选择下拉框中文
time.sleep(5)
# Select(s).select_by_visible_text('中文')
# Select(s).select_by_index(1)
# driver.find_element_by_xpath('//select[@id="Language"]').find_element_by_xpath('//option[text()="中文"]').click()     #直接定位
time.sleep(3)
driver.find_element_by_xpath('//input[contains(@class,"form-control")]').send_keys('APCOMPANY2')
driver.find_element_by_xpath('//input[@id="Password" and @name="Password"]').send_keys('11111a')
driver.find_element_by_xpath('//button[@id="btnSubmit"]').click()     #登录公司账户
time.sleep(2)
s = driver.find_element_by_xpath('//*[@class="form-control"]')      #实例化select
Select(s).select_by_index(0)                                        #下拉框选择索引为0的手机号验证码
time.sleep(3)
# driver.find_element_by_xpath('//*[@class="form-control"]').find_element_by_xpath('//option[@value=1]').click()      #直接定位

driver.find_element_by_xpath('//button[@id=btnSendSms]').click()
driver.find_element_by_id('btnSendSms').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="smsCode"]').send_keys(346751)
driver.find_element_by_xpath('//button[@id="btnNext"]').click()
time.sleep(3)
driver.quit()
#成功登录公司账户,注意验证码需要重新发送，验证码会过期,若输入多次错误密码会导致账户被冻结，慎用

# 总结：定位select下拉框option元素时可采用二次定位方式，
# 三种方式：
# Select(s).select_by_index(0)
# Select(s).select_by_value('value值')
# Select(s).select_by_visible_text('可视化文本')
# 首先导入select：from selenium.webdriver.support.select import Select
# 例如：
# 首先选中定位的select下拉框 ：s=driver.find_by_element_xpath('//select[@元素=‘该元素属性’]')
# 使用二次定位方式定位下拉框：
# 1.通过index下标索引定位：Select(s).select_by_index(0)
# 2.使用value值（若option元素带有value属性）：Select(s).select_by_value('value值')
# 3.使用可视化文本：Select(s).select_by_visible_text('可视化文本')

# 或直接定位：
# 例如：driver.find_element_by_xpath('//select[@id="Language"]').find_by_element_xpath('//option[@元素=‘属性’]')