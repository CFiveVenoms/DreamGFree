from selenium import webdriver
import time
# for case in range(20):
#     browser = webdriver.Firefox()
#     browser.get('http://testpc.etohui.com/login/login.html?callback=/index.html')
#     browser.find_element_by_id('textAccount').click()
#     browser.find_element_by_id('phone').send_keys(18888888868+case)
#     time.sleep(1)
#     browser.find_element_by_id('getCode').click()
#     ################################################################################
#     browser.find_element_by_id('pwd_1').send_keys('123456a')
#     browser.find_element_by_id('pwd_2').send_keys('123456a')
#     ################################################################################
#     browser.find_element_by_xpath('/html/body/article[1]/div/div/ul[2]/div[2]/i/input').click()
#     time.sleep(15)
#     browser.find_element_by_id('account').click()

lists = {"chrome":'threading','id':'webdriver','ff':'python'}
print(lists.items())


