import requests

url = 'http://210.31.32.126/cgi-bin/do_login'
postdata = {'username': '你的校园网账号',
            'password': '{TEXT}你的校园网密码',
            'drop': '0',
            'type': '1',
            'n': '100'}
headers = {'Accept': '*/*',
           'Accept-Encoding': 'gzip, deflate',
           'Accept-Language': 'zh-CN,zh;q=0.8',
           'Connection': 'keep-alive',
           'Content-Length': '65',
           'Content-Type': 'application/x-www-form-urlencoded',
           'Cookie': 'PHPSESSID=a70fr8pfvhhtt329qvb21p7ka6',
           'Host': '210.31.32.126',
           'Origin': 'http://210.31.32.126',
           'Referer': 'http://210.31.32.126/',
           'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'}
# s = requests.Session()
# s.headers = postheader
# r = s.post(url, data=postdata, verify=False)
# print(r.status_code)
requests.post(url, headers=headers, data=postdata)