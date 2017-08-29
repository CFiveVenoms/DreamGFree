import requests
import public.user_Login as lg
import json
import UserCase.user_submitOrder as sb
import random
def get_userOrders():
    Url  = "http://"
    Cookie = lg.post_UserLogin()
    #构造用户Header
    Header = {
        "Cookie":Cookie
    }
    result = requests.get(url=Url,headers =Header)
    if result.status_code==200:
        return json.loads(result.content)
    else:
        print(json.loads(result.content))


################################################################################
# 获取用户的持仓列表中的订单列表（订单号和品种ID）
def get_VarietyPositionOrders(Header):
    orderId_List = []
    Url  = "http://"
    result = requests.get(url=Url, headers=Header)
    data = json.loads(result.content)['data']
    # 首先判断用户是否有持仓，如果为空，首先去购买
    if len(data)==0:
        direction  = random.randint(1,2)
        print(direction)
        if direction==1:
            sb.post_submitOrder_case1(Header)
        elif direction==2:
            sb.post_submitOrder_case2(Header)
        # 重新获取持仓列表
        result = requests.get(url=Url, headers=Header)
        data = json.loads(result.content)['data']
    for list in data:
        showId = list['data'][0]['showId']
        varietyId = list['data'][0]['varietyId']
        orderId = {
            'showId':showId,
            'varietyId':varietyId
        }
        orderId_List.append(orderId)
    return orderId_List
################################################################################
"""
获取用户持仓列表
"""
def get_Orders_List(Header):
    Url  = "http://"
    result = requests.get(url=Url, headers=Header)
    data = json.loads(result.content)['data']
    return  data