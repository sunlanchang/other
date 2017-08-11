# coding=utf-8
#利用selenium操作火狐浏览器进行简单的抢名额，北理暑假集训抢参观阿里名额
from selenium import webdriver
import requests

# url = "https://www.sojump.hk/jq/15455229.aspx"
url = "http://www.sojump.hk/jq/15553463.aspx"
driver = webdriver.Firefox()
driver.get(url)

while True:
    html = requests.get(url).text
    if html.find("很抱歉") == -1:
        driver.get(url)
        driver.find_element_by_id("q1").send_keys("孙兰昌")
        driver.find_element_by_id("q2").send_keys("17301396273")
        driver.find_element_by_id("submit_button").click()
        driver.quit()
        break
    else:
        driver.refresh()
