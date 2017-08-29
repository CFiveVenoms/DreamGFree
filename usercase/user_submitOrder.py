import requests
import UserCase.user_get_HallVariety as ls
import random
###################################################################
Url = "http://forex"
list = ls.get_HallVariety()
length = len(list)
numbers  = random.randint(1,5)
###################################################################
"""
case1 : 用户市价 - 买入 - 0.01手
"""
def post_submitOrder_case1(Header):
    for number in range(numbers) :
        index = random.randrange(length)
        case = {
            'buyType':0,
            'direction':1,
            'varietyId':list[index]
        }
        requests.post(url=Url,data=case,headers = Header)
###################################################################
"""
case2 : 用户市价 - 卖出 - 0.01手
"""
def post_submitOrder_case2(Header):
    for number in range(numbers):
        index = random.randrange(length)
        case = {
            'buyType':0,
            'direction':0,
            'expirationTime':None,
            'varietyId':list[index]
        }
        requests.post(url=Url,data=case,headers = Header)
###################################################################
"""
case3 : 挂单 - 卖出 - 0.01手
"""
def post_submitOrder_case3(Header):
    for number in range(numbers):
        index  = random.randrange(length)
        case = {
            'buyType':1,                     #  买入类型（0 市价，1 挂单）
            'direction':0,                   # 0 卖出，1 买入
                # 品种ID
        }
        requests.post(url=Url,data=case,headers = Header)
###################################################################
"""
case4: 挂单 - 买入 - 0.01手
"""
def post_submitOrder_case4(Header):
    for number in range(numbers):
        index = random.randrange(length)
        case = {
            'buyType':1,                     #  买入类型（0 市价，1 挂单）
            'direction':1,                   # 0 卖出，1 买入
            'expirationTime':'2017/08/04 16:00',         #  挂单的时候 必填，精确到秒
         # 止盈价
            'varietyId':list[index]                  # 品种ID
        }
        requests.post(url=Url,data=case,headers = Header)
###################################################################