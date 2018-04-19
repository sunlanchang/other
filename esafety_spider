import requests
from bs4 import BeautifulSoup


class Spider(object):
    def __init__(self):
        self.url_detail = "http://www.esafety.cn/case/121844.html"
        self.url_items = "http://www.esafety.cn/shiguanli/List_109_10.html"

    def get_url_num(self):
        html = requests.get(self.url_items).content.decode('utf-8')
        soup = BeautifulSoup(html, 'lxml')

    def get_data(self):
        html = requests.get(self.url_detail).content.decode('utf-8')
        soup = BeautifulSoup(html, 'lxml')
        data_tag = soup.select('.c_content_text')[0]
        data_text = data_tag.text.strip()
        return data_text

    def save(self, data):
        with open('a.txt', 'w', encoding='utf-8') as f:
            f.write(data)


s = Spider()
data = s.get_data()
s.save(data)
# s.get_url_num()
