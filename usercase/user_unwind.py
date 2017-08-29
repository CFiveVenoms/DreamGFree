import UserCase.user_getVarietyPositionOrders as lt

import requests
import json
"""
用户平仓
"""
def user_Unwind(Header):
    Url = "http://forex2"
    list = lt.get_VarietyPositionOrders(Header)
    # 在平仓之前进行一次查询，如果用户仓库为空，首先执行购买，让后在执行的平仓
    for orderid in list:
        data = {
            'direction': 0 ,
            'handsNum':0.01 ,
            'showId' :orderid['showId'] ,
            'varietyId': orderid['varietyId'],
            'unwindPrice': 30.000,
        }
        result = requests.post(url=Url,data = data,headers=Header)
        print(json.loads(result.content))