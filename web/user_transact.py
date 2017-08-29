from selenium import webdriver
import time
import UserCase.user_getVarietyPositionOrders as od
import UserCase.user_submitOrder as sb # 持仓
import UserCase.user_unwind as un   # 平仓
import random

def user_Login():
    tokens = []
    for i in range(20):
        borwser = webdriver.Firefox()
        borwser.get('http://forex2')
        borwser.find_element_by_id('phone').send_keys(18860+i)
        borwser.find_element_by_id('pwd').send_keys('')
        borwser.find_element_by_xpath('/html/body/div[1]/div[2]').click()
        time.sleep(2)
        borwser.find_element_by_link_text('订单').click()
        cookie = [item["name"] + "=" + item["value"] for item in borwser.get_cookies()]
        cookiestr = ';'.join(item for item in cookie)
        token = {'Cookie':cookiestr}
        tokens.append(token)
    return tokens

def user_OneLogin():
    borwser = webdriver.Firefox()
    borwser.get('http://forex2')
    borwser.find_element_by_id('phone').send_keys()
    borwser.find_element_by_id('pwd').send_keys('')
    borwser.find_element_by_xpath('/html/body/div[1]/div[2]').click()
    borwser.find_element_by_link_text('订单').click()
    cookie = [item["name"] + "=" + item["value"] for item in borwser.get_cookies()]
    cookiestr = ';'.join(item for item in cookie)
    token  = {
        "Cookie":cookiestr
    }
    print(od.get_VarietyPositionOrders(token))
def Hang_Up(tokens):
    for token in tokens:
        count = random.randint(1,3)
        # 创建线程  1：购买，2：平仓 ；3 查询
        if count==1:
            sb.post_submitOrder_case1(token)
        elif count==2:
            un.user_Unwind(token)
        elif count==3:
            od.get_Orders_List(token)


##################################################################################
# 定时任务 - 持续执行 - 到周六早上5点结束
endTime = '2017-08-29 13:00:00'
currentTime = int(time.time())
#转换为时间数组
timeArray = time.strptime(endTime,'%Y-%m-%d %H:%M:%S')
#转换为时间戳
endTime = int(time.mktime(timeArray))
number = endTime - currentTime
tokens = user_Login()
for i in range(number):
    Hang_Up(tokens)
##################################################################################

