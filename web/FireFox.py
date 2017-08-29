from selenium import webdriver
import time
import web.userLogin_result as lg
Users = lg.get_user()
for user in Users:
    browser = webdriver.Firefox()
    error  = ''
    browser.get('https://www.etohui.com/login/login.html?callback=/index.html')
    browser.find_element_by_id('dlPhone').send_keys(user['dlPhone'])
    browser.find_element_by_id('dlPassword').send_keys(user['dlPassword'])
    browser.find_element_by_id('loginIndex').click()
    time.sleep(3)
    try :
       error = browser.find_element_by_xpath('/html/body/article[1]/div/div/ul[1]/div[1]/p').text
       print(error)
    except:
        error = "登录成功"
        print(error)
