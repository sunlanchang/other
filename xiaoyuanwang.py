#ubuntu实现自动启动此脚本
#root权限修改/etc/rc.local文件在exit 0上一行加上 python3 xiaoyuanwang.py
#即可实现开机启动此脚本

#python 2.7 python 3.5均可用
#脚本外部依赖requests库，请在运行脚本前pip3或者pip安装requests

#python 2.7运行时务必加上下面一行代码，指定编码为utf8，python3可以忽略。
# coding: utf-8
import requests


url = 'http://210.31.32.126/cgi-bin/do_login'


def login():
    postdata = {'username': '你的校园网账号',
                'password': '{TEXT}你的密码',
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
    requests.post(url, data=postdata)


def is_connect_edu():
    status_code = requests.get(url).status_code
    if status_code == 200:
        return True
    else:
        return False


def is_connect_web():
    r = requests.get("http://www.baidu.com").text
    if r.find('210.31.32.126') != -1:
        return False
    else:
        return True


while True:
    if is_connect_edu():  # 是否连接上校园网
        if not is_connect_web():  # 是否连接上外网
            login()
            if requests.get('http://www.baidu.com').status_code==200:
                print('Already connected Internet')
            else:
                print('Not connected Internet')
        break
