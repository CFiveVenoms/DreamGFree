import requests
import json
def get_HallVariety():
    url = "http://www.baidu.com" # 这里是举例，填写属于自己登录密码
    list = []
    result_list = requests.get(url=url)
    for id in json.loads(result_list.content)['data']:
        varietyId  = id['varietyId']
        list.append(varietyId)
    return list

