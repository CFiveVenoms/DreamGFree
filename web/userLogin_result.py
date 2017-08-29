import xlrd
from selenium import webdriver
from xlutils.copy import copy
import time
data = xlrd.open_workbook(u'D:\\PycharmProjects\\etonhui_\\xls\\userLogin.xls')
sheet0 = data.sheets()[0]
nrows = sheet0.nrows
error  = ''
wb = copy(data)
s = wb.get_sheet(0)
for user in range(2,nrows):
    dlPhone = int(sheet0.row_values(user)[1])
    dlPassword = sheet0.row_values(user)[2]
    # 读取用户信息后执行登录操作
    browser = webdriver.Firefox()
    browser.get('https://www')
    browser.find_element_by_id('dlPhone').send_keys(dlPhone)
    browser.find_element_by_id('dlPassword').send_keys(dlPassword)
    browser.find_element_by_id('loginIndex').click()
    time.sleep(1)
    try:
        error = browser.find_element_by_xpath('/html/body/article[1]/div/div/ul[1]/div[1]/p').text
    except:
        error = "登录成功"
    finally:
        s.write(user,4,error)
        browser.quit()
# wb.save("D:\\PycharmProjects\\etonhui_\\xls\\userLogin.xls")
wb.save()

