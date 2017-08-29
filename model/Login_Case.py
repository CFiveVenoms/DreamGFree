import requests
import json
def post_userLogin_case():
    url = ""
    user = {
        'userPhone':'18888888888',
        'userPass':'123456a'
    }
    result = requests.post(url=url,params = user)
    print(json.loads(result.content))
post_userLogin_case()