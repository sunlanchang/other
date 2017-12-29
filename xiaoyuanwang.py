#ubuntu实现自动启动此脚本
#root权限修改/etc/rc.local文件在exit 0上一行加上 python3 xiaoyuanwang.py
#即可实现开机启动此脚本

#python 2.7 python 3.5均可用
#脚本外部依赖requests库，请在运行脚本前pip3或者pip安装requests

#python 2.7运行时务必加上下面一行代码，指定编码为utf8，python3可以忽略。
# coding: utf-8
import requests

url = 'http://210.31.32.126/cgi-bin/do_login'
url1 = 'http://210.31.32.126/cgi-bin/keeplive'
url2 = 'http://210.31.32.126/user_info.php?uid='
url3 = 'http://210.31.32.126//cgi-bin/do_logout'


def login():
    postdata = {'username': '5120150752',
                'password': '{TEXT}bipt184755',
                'drop': '0',
                'type': '1',
                'n': '100'}
    a = requests.post(url, data=postdata).content
    print "******Internet connected!"  # ,uid is",('%s' %a)
    c = url2 + a
    # print c
    d = requests.get(c).content
    # print d
    e = str('10.10')
    f = d.find(e)
    # print f


def usage():
    b = requests.get(url1).content
    # print "usageinfo is"
    b = (b.split(','))
    online_time = int(b[0]) / 60
    traffic_out = int(b[2])
    traffic_in = int(b[1])
    balance = int(b[3])
    balance_left = float(balance - traffic_in - traffic_out) / 1000000000
    usage_this_session = float(traffic_in + traffic_out) / 1000000
    # print online_time,traffic_out,traffic_in,balance
    print ('***Online for %d minutes.' % online_time)
    print ('***Data used this session %.2f M' % usage_this_session)
    print ('***Balance left %.3f G' % balance_left)


login()
usage()

