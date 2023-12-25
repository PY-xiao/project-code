import os, django
import sys
path = os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)
# print(sys.path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "JD.settings")  # project_name 项目名称
django.setup()

import requests
import re
import json
import time
from bs4 import BeautifulSoup
import traceback

from django.db.models import Q
from Electronics import models
import traceback



# 定义函数抓取每页前30条商品信息
def crow_first(n):
    # 构造每一页的url变化
    url = 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&cid2=653&cid3=655&page=' + str(
        2 * n - 1)
    head = {'authority': 'search.jd.com',
            'method': 'GET',
            'path': '/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=4&s=84&scrolling=y&log_id=1529828108.22071&tpl=3_M&show_items=7651927,7367120,7056868,7419252,6001239,5934182,4554969,3893501,7421462,6577495,26480543553,7345757,4483120,6176077,6932795,7336429,5963066,5283387,25722468892,7425622,4768461',
            'scheme': 'https',
            'referer': 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=3&s=58&click=0',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'Cookie': 'qrsc=3; pinId=RAGa4xMoVrs; xtest=1210.cf6b6759; ipLocation=%u5E7F%u4E1C; _jrda=5; TrackID=1aUdbc9HHS2MdEzabuYEyED1iDJaLWwBAfGBfyIHJZCLWKfWaB_KHKIMX9Vj9_2wUakxuSLAO9AFtB2U0SsAD-mXIh5rIfuDiSHSNhZcsJvg; shshshfpa=17943c91-d534-104f-a035-6e1719740bb6-1525571955; shshshfpb=2f200f7c5265e4af999b95b20d90e6618559f7251020a80ea1aee61500; cn=0; 3AB9D23F7A4B3C9B=QFOFIDQSIC7TZDQ7U4RPNYNFQN7S26SFCQQGTC3YU5UZQJZUBNPEXMX7O3R7SIRBTTJ72AXC4S3IJ46ESBLTNHD37U; ipLoc-djd=19-1607-3638-3638.608841570; __jdu=930036140; user-key=31a7628c-a9b2-44b0-8147-f10a9e597d6f; areaId=19; __jdv=122270672|direct|-|none|-|1529893590075; PCSYCityID=25; mt_xid=V2_52007VwsQU1xaVVoaSClUA2YLEAdbWk5YSk9MQAA0BBZOVQ0ADwNLGlUAZwQXVQpaAlkvShhcDHsCFU5eXENaGkIZWg5nAyJQbVhiWR9BGlUNZwoWYl1dVF0%3D; __jdc=122270672; shshshfp=72ec41b59960ea9a26956307465948f6; rkv=V0700; __jda=122270672.930036140.-.1529979524.1529984840.85; __jdb=122270672.1.930036140|85.1529984840; shshshsID=f797fbad20f4e576e9c30d1c381ecbb1_1_1529984840145'
            }
    r = requests.get(url, headers=head)
    # print(r.text)
    # 指定编码方式，不然会出现乱码
    r.encoding = 'utf-8'
    html1 = BeautifulSoup(r.text,'html.parser')
    # 定位到每一个商品标签li
    datas = html1.select('li.gl-item')
    # 将抓取的结果保存到本地CSV文件中
    for data in datas:
        try:
            time.sleep(1)
            dicts1 = {}
            p_price = data.select('div > div.p-price > strong > i')
            if len(p_price) == 0:
                p_price = data.select ('div > div.p-price > strong > data-price')
            p_price = p_price[0].text.strip()
            dicts1['price'] = p_price
            name = data.select('div.p-name.p-name-type-2  em')[0].text.strip()
            dicts1['name'] = name
            lianjie = data.select('div.p-commit > strong > a')[0].attrs.get('href')
            if 'https' not in lianjie:
                lianjie = 'https:' + lianjie
            dicts1['url'] = lianjie
            shopname = data.select('a.curr-shop.hd-shopname')[0].text.strip()
            dicts1['shopname'] = shopname
            id = re.findall('(\d+).html',lianjie)[0]
            html = requests.get(url=lianjie,headers=head)
            soup = BeautifulSoup(html.text,'html.parser')
            pinbai = soup.select('div.inner.border a')[0].text.strip()
            dicts1['pinbai'] = pinbai
            xinghao = soup.select('div.item.ellipsis')[0].text.strip()
            dicts1['xinghao'] = xinghao
            url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={}&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'.format(id)
            html = requests.get(url=url,headers=head)
            contnt = re.findall('fetchJSON_comment98\((.*)\)',html.text)
            json_info = json.loads(str(contnt[0]))
            haoping = json_info['productCommentSummary']['goodRateShow']
            haoping = str(haoping).replace('+','').replace('万','0000')
            dicts1['haoping'] = haoping
            chaping = json_info['productCommentSummary']['poorCountStr']
            chaping = str(chaping).replace('+','').replace('万','0000')
            dicts1['chaping'] = chaping
            count = json_info['productCommentSummary']['commentCountStr']
            count = str(count).replace('+','').replace('万','0000')
            dicts1['count'] = count
            print(dicts1)
            if not models.XinXi.objects.filter(name=dicts1['name']).filter(url=dicts1['url']):
                            models.XinXi.objects.create(
                                name=dicts1['name'],
                                url=dicts1['url'],
                                price=dicts1['price'],
                                shopname=dicts1['shopname'],
                                pinpai=dicts1['pinbai'],
                                xinghao=dicts1['xinghao'],
                                haoping=dicts1['haoping'],
                                chaping=dicts1['chaping'],
                                count=dicts1['count']
                            )
            else:
                models.XinXi.objects.filter(name=dicts1['name']).filter(url=dicts1['url']).update(
                    price=dicts1['price'],
                    shopname=dicts1['shopname'],
                    pinpai=dicts1['pinbai'],
                    xinghao=dicts1['xinghao'],
                    haoping=dicts1['haoping'],
                    chaping=dicts1['chaping'],
                    count=dicts1['count']
                )
        except:
            print(traceback.format_exc())


# 定义函数抓取每页后30条商品信息
def crow_last(n):
    # 获取当前的Unix时间戳，并且保留小数点后5位
    a = time.time()
    b = '%.5f' % a
    url = 'https://search.jd.com/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=' + str(
        2 * n) + '&s=' + str(48 * n - 20) + '&scrolling=y&log_id=' + str(b)
    head = {'authority': 'search.jd.com',
            'method': 'GET',
            'path': '/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA',
            'scheme': 'https',
            'referer': 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=3&s=58&click=0',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'Cookie': 'qrsc=3; pinId=RAGa4xMoVrs; xtest=1210.cf6b6759; ipLocation=%u5E7F%u4E1C; _jrda=5; TrackID=1aUdbc9HHS2MdEzabuYEyED1iDJaLWwBAfGBfyIHJZCLWKfWaB_KHKIMX9Vj9_2wUakxuSLAO9AFtB2U0SsAD-mXIh5rIfuDiSHSNhZcsJvg; shshshfpa=17943c91-d534-104f-a035-6e1719740bb6-1525571955; shshshfpb=2f200f7c5265e4af999b95b20d90e6618559f7251020a80ea1aee61500; cn=0; 3AB9D23F7A4B3C9B=QFOFIDQSIC7TZDQ7U4RPNYNFQN7S26SFCQQGTC3YU5UZQJZUBNPEXMX7O3R7SIRBTTJ72AXC4S3IJ46ESBLTNHD37U; ipLoc-djd=19-1607-3638-3638.608841570; __jdu=930036140; user-key=31a7628c-a9b2-44b0-8147-f10a9e597d6f; areaId=19; __jdv=122270672|direct|-|none|-|1529893590075; PCSYCityID=25; mt_xid=V2_52007VwsQU1xaVVoaSClUA2YLEAdbWk5YSk9MQAA0BBZOVQ0ADwNLGlUAZwQXVQpaAlkvShhcDHsCFU5eXENaGkIZWg5nAyJQbVhiWR9BGlUNZwoWYl1dVF0%3D; __jdc=122270672; shshshfp=72ec41b59960ea9a26956307465948f6; rkv=V0700; __jda=122270672.930036140.-.1529979524.1529984840.85; __jdb=122270672.1.930036140|85.1529984840; shshshsID=f797fbad20f4e576e9c30d1c381ecbb1_1_1529984840145'

            }
    r = requests.get(url, headers=head)
    r.encoding = 'utf-8'
    html1 = BeautifulSoup(r.text,'html.parser')
    datas = html1.select('li.gl-item')
    for data in datas:
        time.sleep(1)
        try:
            dicts1 = {}
            p_price = data.select('div > div.p-price > strong > i')
            if len(p_price) == 0:
                p_price = data.select('div > div.p-price > strong > data-price')
            p_price = p_price[0].text.strip()
            dicts1['price'] = p_price
            name = data.select('div.p-name.p-name-type-2  em')[0].text.strip()
            dicts1['name'] = name
            lianjie = data.select('div.p-commit > strong > a')[0].attrs.get('href')
            if 'https' not in lianjie:
                lianjie = 'https:' + lianjie
            dicts1['url'] = lianjie
            shopname = data.select('a.curr-shop.hd-shopname')[0].text.strip()
            dicts1['shopname'] = shopname
            id = re.findall('(\d+).html', lianjie)[0]
            html = requests.get(url=lianjie, headers=head)
            soup = BeautifulSoup(html.text, 'html.parser')
            pinbai = soup.select('div.inner.border a')[0].text.strip()
            dicts1['pinbai'] = pinbai
            xinghao = soup.select('div.item.ellipsis')[0].text.strip()
            dicts1['xinghao'] = xinghao
            url = 'https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId={}&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1'.format(
                id)
            html = requests.get(url=url, headers=head)
            contnt = re.findall('fetchJSON_comment98\((.*)\)', html.text)
            json_info = json.loads(str(contnt[0]))
            haoping = json_info['productCommentSummary']['goodRateShow']
            haoping = str(haoping).replace('+','').replace('万','0000')
            dicts1['haoping'] = haoping
            chaping = json_info['productCommentSummary']['poorCountStr']
            chaping = str(chaping).replace('+','').replace('万','0000')
            dicts1['chaping'] = chaping
            count = json_info['productCommentSummary']['commentCountStr']
            count = str(count).replace('+','').replace('万','0000')
            dicts1['count'] = count
            print(dicts1)
            if not models.XinXi.objects.filter(name=dicts1['name']).filter(url=dicts1['url']):
                            models.XinXi.objects.create(
                                name=dicts1['name'],
                                url=dicts1['url'],
                                price=dicts1['price'],
                                shopname=dicts1['shopname'],
                                pinpai=dicts1['pinbai'],
                                xinghao=dicts1['xinghao'],
                                haoping=dicts1['haoping'],
                                chaping=dicts1['chaping'],
                                count=dicts1['count']
                            )
            else:
                models.XinXi.objects.filter(name=dicts1['name']).filter(url=dicts1['url']).update(
                    price=dicts1['price'],
                    shopname=dicts1['shopname'],
                    pinpai=dicts1['pinbai'],
                    xinghao=dicts1['xinghao'],
                    haoping=dicts1['haoping'],
                    chaping=dicts1['chaping'],
                    count=dicts1['count']
                )
        except:
            print(traceback.format_exc())


def start():
    for i in range(1, 5):
        # 下面的print函数主要是为了方便查看当前抓到第几页了
        try:
            crow_first(i)
        except Exception as e:
            print(traceback.format_exc())
        try:
            crow_last(i)
        except Exception as e:
            print(traceback.format_exc())

if __name__ == '__main__':
    start()