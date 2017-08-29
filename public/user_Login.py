import requests
def post_UserLogin():
    Url  = "URL地址"
    data = {
        'userPhone':'18888888862',
        'userPass':'123456a'
    }
    result = requests.post(url=Url,data=data)
    if len(result.cookies)> 0 :
        tooken1 = result.cookies.items()[0][1]
        tooken2 = result.cookies.items()[1][1]
        #构造用户tooken携带信息
        Cookie = 'token1='+tooken1+';token2='+tooken2
        return Cookie
    else:
        print("用户登录失败")