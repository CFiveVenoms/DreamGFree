import requests
import json
import public.Report_xlsx
import public.SempEmail
################################################################################################
################################################################################################
def post_userLogin():
    url = "http://forex"
    user = {
        'userPhone':'18888888889',
        'userPass':'123456a'
    }
    request = requests.post(url=url,params = user)
    #获取用户登录后携带的token信息，用于后续的查询操作
    cookie1 = request.cookies.items()[0][1]
    cookie2 = request.cookies.items()[1][1]
    #拼凑成我们想要的Cookies
    Cookie = "token1="+cookie1+";token2="+cookie2
    return Cookie
################################################################################################
################################################################################################
def post_userLogin_case():
    url = "http://forex2"
    user = {
        'userPhone':'18888888889',
        'userPass':'123456a'
    }
    result = requests.post(url=url,params = user)
    content = json.loads(result.content)
    length = len(content['data'])
    status = result.status_code
    result = result_back(status=status, length=length)
    return result
def result_back(status,length):
    data = []
    if status != 200:
        # data =  "请求连接失败"
        data = "error"
    elif status == 200 and length <= 0:
        # data  = "请求内容为空"
        data = "warning"
    elif status == 200 and length > 0:
        # data = "测试通过"
        data = "pass"
    else:
        data = status
    return data
################################################################################################
def get_getVarietyPositionOrders():
    data  = []
    Cookie = post_userLogin()
    # 获取用户订单列表的URL地址
    url  = "http://forex2"
    #模拟用户请求 首先需要传递请求头中的Header信息 Cookie
    Headers = {
        'Cookie':Cookie
    }
    # 订单的分页参数 (如果没有参数，提示请求参数不正确)
    params = {
        "pageNo": 1,
        "pageSize": 20
    }
    result = requests.get(url=url,params = params , headers = Headers)
    content = json.loads(result.content)
    length = len(content['data'])
    status = result.status_code
    result = result_back(status=status,length=length)
    return result
###############################################################################################
data = [get_getVarietyPositionOrders(),post_userLogin_case()]
pass_count=0
error_count=0
warning_count=0
for i in data:
    result = i
    if result=='pass':
        pass_count +=1
    elif result =="error":
        error_count +=1
    elif result =="warning":
        warning_count +=1
################################################
if __name__ == '__main__':
    # 执行测试报告编写
    public.Report_xlsx.get_sheet1("V1.1.0", len(data), pass_count=pass_count, error_count=error_count)
    public.SempEmail.put_Emal()
###############################################

