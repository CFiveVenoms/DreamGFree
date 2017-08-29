import requests
import json
import public.user_Login as lg
import time
def post_Unwind():
    Url = "http://test"
    data = {
        'direction': 0 ,
        'handsNum':0.01 ,

    }
    Cookie =  lg.post_UserLogin()
    Header  = {
        'Cookie':Cookie
    }
    result = requests.post(url=Url,data = data,headers=Header)
    print(json.loads(result.content))
print("开始普通订单攻击")
start  = time.clock()
for i in range(100):
    post_Unwind()
end = time.clock()
print("普通订单刷单耗时 %f s" %(start - end))

