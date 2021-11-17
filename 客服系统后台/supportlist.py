from selenium import webdriver
driver=webdriver.Chrome()

driver.get('https://wbx3-hdagent.ovivas.cn/Account/Login')
driver.find_element_by_xpath('//*[@id="Language"]/option[2]').click()
driver.find_element_by_name('UserName').send_keys('q11111q')
driver.find_element_by_name('Password').send_keys('123456a')
driver.find_element_by_id('btnSubmit').click()

driver.get('https://wbx3-hdagent.ovivas.cn/#/SupportList')
driver.find_element_by_xpath('//input[@placeholder="请输入账号"]').send_keys('KFJL01')
driver.find_element_by_xpath('//button[@id="searchBtn"]').send_keys()





# <input type="text" id="txtUserId" class="form-control m-input" style="width:500px;" placeholder="请输入账号" data-col-index="0">
#
# < button
#
#
# class ="btn btn-brand m-btn m-btn--icon right" id="searchBtn" >
#
# < span >
# < i
#
#
# class ="la la-search" > < / i >
#
# < span >
# 查询
# < / span >
# < / span >
# < / button >