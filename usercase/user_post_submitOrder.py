"""
@author : 汤中华
@diction : 主要检测用户违法创建订单
"""
import requests
import public.user_Login as lg
import UserCase.user_get_HallVariety as ls
import json
import time
# ----------- 构建全局使用参数
# -------------------------------------------
Url = "http://testpc"
Cookie = lg.post_UserLogin()
Header = {
    "Cookie": Cookie
}
list = ls.get_HallVariety()
"""
case1 : 用户市价 - 买入 - 0.01手
"""
def post_submitOrder_case1():
    for vid in list :
        case = {
            'buyType':0,
            'direction':1,

        }
        result  = requests.post(url=Url,data=case,headers = Header)
        print(json.loads(result.content))
    print("-----------------------------------------------------")
"""
case2 : 用户市价 - 卖出 - 0.01手
"""
def post_submitOrder_case2():
    for vid in list :
        case = {
            'buyType':0,
            'direction':0,
            'expirationTime':None,

        }
        result  = requests.post(url=Url,data=case,headers = Header)
        print(json.loads(result.content))
    print("-----------------------------------------------------")
"""
case3 : 挂单 - 卖出 - 0.01手
"""
def post_submitOrder_case3():
    for vid in list :
        case = {
            'buyType':1,                     #  买入类型（0 市价，1 挂单）
            'direction':0,                   # 0 卖出，1 买入
            'expirationTime':'2017/08/03 16:00',         #  挂单的时候 必填，精确到秒
        }
        result  = requests.post(url=Url,data=case,headers = Header)
        print(json.loads(result.content))
    print("-----------------------------------------------------")
"""
case4: 挂单 - 买入 - 0.01手
"""
def post_submitOrder_case4():
    list = [90]
    for vid in list :
        case = {
            'buyType':1,                     #  买入类型（0 市价，1 挂单）
            'direction':1,                   # 0 卖出，1 买入
            'expirationTime':'2017/08/04 16:00',         #  挂单的时候 必填，精确到秒
            'handsNum':0.01,                 # 手数
        }
        result  = requests.post(url=Url,data=case,headers = Header)
        print(json.loads(result.content))
    print("-----------------------------------------------------")
if __name__ == '__main__':
    # post_submitOrder_case1()
    # post_submitOrder_case2()
    # post_submitOrder_case3()
    post_submitOrder_case4()