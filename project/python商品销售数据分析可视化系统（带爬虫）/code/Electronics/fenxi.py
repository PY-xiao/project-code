import os, django
import sys
path = os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(path)
# print(sys.path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "JD.settings")  # project_name 项目名称
django.setup()

import matplotlib.pyplot as plt
from pylab import *
import copy

from django.db.models import Q
from Electronics import models

plt.rcParams['font.sans-serif'] = ['SimHei']

def danjia_section():
    num1 = len(models.XinXi.objects.filter(Q(price__gt=0) & Q(price__lte=1000)))
    num2 = len(models.XinXi.objects.filter(Q(price__gt=1000) & Q(price__lte=2000)))
    num3 = len(models.XinXi.objects.filter(Q(price__gt=2000) & Q(price__lte=3000)))
    num4 = len(models.XinXi.objects.filter(Q(price__gt=3000) & Q(price__lte=4000)))
    num5 = len(models.XinXi.objects.filter(Q(price__gt=4000) & Q(price__lte=100000)))
    lists = [num1,num2,num3,num4,num5]
    lists.sort()


    plt.figure(figsize=(8, 6), dpi=80)

    # 再创建一个规格为 1 x 1 的子图
    plt.subplot(1, 1, 1)

    # 柱子总数
    N = 5
    # 包含每个柱子对应值的序列
    values = (num1,num2,num3,num4,num5)

    # 包含每个柱子下标的序列
    index = np.arange(N)

    # 柱子的宽度
    width = 0.35

    # 绘制柱状图, 每根柱子的颜色为紫罗兰色
    p2 = plt.bar(index, values, width, label="手机各价格区间数量", color="b")

    # 设置横轴标签
    plt.xlabel('价格')
    # 设置纵轴标签
    plt.ylabel('数量')

    # 添加标题
    plt.title('手机各价格区间数量')

    # 添加纵横轴的刻度
    plt.xticks(index, ('0-1000', '1000-2000', '2000-3000', '3000-4000', '4000以上'))
    plt.yticks()

    # 添加图例
    plt.legend(loc="upper right")

    for rect in p2:  # rects 是三根柱子的集合
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), size=15, ha='center', va='bottom')

    path = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))) + os.sep + 'static' + os.sep + 'fenxi_img'
    if not os.path.exists(path):
        os.makedirs(path)
    paths = path + os.sep + 'danjia_section.jpg'
    print("pahts:",paths)
    plt.savefig(paths, dpi=100)
    plt.close()


def bing_danjia():
    num1 = len(models.XinXi.objects.filter(Q(price__gt=0) & Q(price__lte=1000)))
    num2 = len(models.XinXi.objects.filter(Q(price__gt=1000) & Q(price__lte=2000)))
    num3 = len(models.XinXi.objects.filter(Q(price__gt=2000) & Q(price__lte=3000)))
    num4 = len(models.XinXi.objects.filter(Q(price__gt=3000) & Q(price__lte=4000)))
    num5 = len(models.XinXi.objects.filter(Q(price__gt=4000) & Q(price__lte=100000)))

    labels = ['0-1000', '1000-2000', '2000-3000', '3000-4000', '4000以上']
    sizes = [num1,num2,num3,num4,num5]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','red']
    explode = (0, 0.1, 0, 0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)

    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    plt.title('手机各价格区间饼图')

    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep + 'static' +  os.sep + 'fenxi_img'
    if not os.path.exists(path):
        os.makedirs(path)
    paths = path + os.sep +'bing_danjia.jpg'
    plt.savefig(paths,dpi=100)
    plt.close()


def pinpai_section():
    huawei = len(models.XinXi.objects.filter(Q(pinpai__icontains='华为') | Q(pinpai__icontains='荣耀')))
    xiaomi = len(models.XinXi.objects.filter(Q(pinpai__icontains='小米') | Q(pinpai__icontains='MI')))
    vivo = len(models.XinXi.objects.filter(Q(pinpai__icontains='vivo')))
    oppo = len(models.XinXi.objects.filter(Q(pinpai__icontains='oppo')))
    Apple = len(models.XinXi.objects.filter(Q(pinpai__icontains='Apple')| Q(pinpai__icontains='苹果')))
    lists = [huawei,xiaomi,vivo,oppo,Apple]
    lists.sort()


    plt.figure(figsize=(8, 6), dpi=80)

    # 再创建一个规格为 1 x 1 的子图
    plt.subplot(1, 1, 1)

    # 柱子总数
    N = 5
    # 包含每个柱子对应值的序列
    values = (huawei,xiaomi,vivo,oppo,Apple)

    # 包含每个柱子下标的序列
    index = np.arange(N)

    # 柱子的宽度
    width = 0.35

    # 绘制柱状图, 每根柱子的颜色为紫罗兰色
    p2 = plt.bar(index, values, width, label="前五品牌商品数量", color="b")

    # 设置横轴标签
    plt.xlabel('品牌')
    # 设置纵轴标签
    plt.ylabel('数量')

    # 添加标题
    plt.title('前五品牌商品数量')

    # 添加纵横轴的刻度
    plt.xticks(index, ('华为','小米','vivo','oppo','Apple'))
    plt.yticks()

    # 添加图例
    plt.legend(loc="upper right")

    for rect in p2:  # rects 是三根柱子的集合
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), size=15, ha='center', va='bottom')

    path = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))) + os.sep + 'static' + os.sep + 'fenxi_img'
    if not os.path.exists(path):
        os.makedirs(path)
    paths = path + os.sep + 'pinpai_section.jpg'
    plt.savefig(paths, dpi=100)
    plt.close()


def bing_pinpai():
    huawei = len(models.XinXi.objects.filter(Q(pinpai__icontains='华为') | Q(pinpai__icontains='荣耀')))
    xiaomi = len(models.XinXi.objects.filter(Q(pinpai__icontains='小米') | Q(pinpai__icontains='MI')))
    vivo = len(models.XinXi.objects.filter(Q(pinpai__icontains='vivo')))
    oppo = len(models.XinXi.objects.filter(Q(pinpai__icontains='oppo')))
    Apple = len(models.XinXi.objects.filter(Q(pinpai__icontains='Apple')| Q(pinpai__icontains='苹果')))

    labels = ['华为','小米','vivo','oppo','Apple']
    sizes = [huawei,xiaomi,vivo,oppo,Apple]
    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral','red']
    explode = (0, 0.1, 0, 0,0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=90)

    # Set aspect ratio to be equal so that pie is drawn as a circle.
    plt.axis('equal')
    plt.title('前五品牌商品数量占比饼图')

    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep + 'static' +  os.sep + 'fenxi_img'
    if not os.path.exists(path):
        os.makedirs(path)
    paths = path + os.sep +'bing_pinpai.jpg'
    plt.savefig(paths,dpi=100)
    plt.close()

def chaping_to5():
    datas = models.XinXi.objects.all().order_by('-chaping')[:5]
    # print(datas)
    shopnames = []
    counts = []
    for data in datas:
        shopnames.append(data.shopname)
        counts.append(data.chaping)
    plt.figure(figsize=(10, 8), dpi=80)

    # 再创建一个规格为 1 x 1 的子图
    plt.subplot(1, 1, 1)

    # 柱子总数
    N = 5
    # 包含每个柱子对应值的序列
    values = tuple(counts)

    # 包含每个柱子下标的序列
    index = np.arange(N)

    # 柱子的宽度
    width = 0.35

    # 绘制柱状图, 每根柱子的颜色为紫罗兰色
    p2 = plt.bar(index, values, width, label="差评数最多前五商品", color="b")

    # 设置横轴标签
    plt.xlabel('店铺名')
    # 设置纵轴标签
    plt.ylabel('数量')

    # 添加标题
    plt.title('差评数最多前五商品')

    # 添加纵横轴的刻度
    plt.xticks(index, tuple(shopnames))
    plt.xticks(rotation=-10)
    plt.yticks()

    # 添加图例
    plt.legend(loc="upper right")

    for rect in p2:  # rects 是三根柱子的集合
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), size=15, ha='center', va='bottom')

    path = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))) + os.sep + 'static' + os.sep + 'fenxi_img'
    if not os.path.exists(path):
        os.makedirs(path)
    paths = path + os.sep + 'chaping_section.jpg'
    plt.savefig(paths, dpi=100)
    plt.close()

def haoping_to5():
    datas = models.XinXi.objects.all().order_by('haoping')[:5]
    # print(datas)
    shopnames = []
    counts = []
    for data in datas:
        shopnames.append(data.shopname)
        counts.append(data.haoping)
    plt.figure(figsize=(10, 8), dpi=80)

    # 再创建一个规格为 1 x 1 的子图
    plt.subplot(1, 1, 1)

    # 柱子总数
    N = 5
    # 包含每个柱子对应值的序列
    values = tuple(counts)

    # 包含每个柱子下标的序列
    index = np.arange(N)

    # 柱子的宽度
    width = 0.35

    # 绘制柱状图, 每根柱子的颜色为紫罗兰色
    p2 = plt.bar(index, values, width, label="好评率最高前五商品", color="b")

    # 设置横轴标签
    plt.xlabel('店铺名')
    # 设置纵轴标签
    plt.ylabel('数量')

    # 添加标题
    plt.title('好评率最高前五商品')

    # 添加纵横轴的刻度
    plt.xticks(index, tuple(shopnames))
    plt.xticks(rotation=-10)
    plt.yticks()

    # 添加图例
    plt.legend(loc="upper right")

    for rect in p2:  # rects 是三根柱子的集合
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), size=15, ha='center', va='bottom')

    path = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))) + os.sep + 'static' + os.sep + 'fenxi_img'
    if not os.path.exists(path):
        os.makedirs(path)
    paths = path + os.sep + 'haoping_section.jpg'
    plt.savefig(paths, dpi=100)
    plt.close()

def zhexianyuling():
    # nums.sort()
    num1count,num2count,num3count,num4count,num5count,num6count = 0,0,0,0,0,0
    num1 = models.XinXi.objects.filter(Q(price__gt=0) & Q(price__lte=1000))
    for nums in num1:
        num1count += nums.count
    num2 = models.XinXi.objects.filter(Q(price__gt=1000) & Q(price__lte=2000))
    num3 = models.XinXi.objects.filter(Q(price__gt=2000) & Q(price__lte=3000))
    num4 = models.XinXi.objects.filter(Q(price__gt=3000) & Q(price__lte=4000))
    num5 = models.XinXi.objects.filter(Q(price__gt=4000) & Q(price__lte=5000))
    num6 = models.XinXi.objects.filter(Q(price__gt=5000) & Q(price__lte=100000))
    for nums in num2:
        num2count += nums.count
    for nums in num3:
        num3count += nums.count
    for nums in num4:
        num4count += nums.count
    for nums in num5:
        num5count += nums.count
    for nums in num6:
        num6count += nums.count
    x = ["0-1000","1000-2000","2000-3000","3000-4000","4000-5000",">5000"]
    y = [num1count,num2count,num3count,num4count,num5count,num6count]
    plt.figure(figsize=(10, 8), dpi=80)
    print(x)
    print(y)
    # "r" 表示红色，ms用来设置*的大小
    plt.plot(x, y, "r", marker='*', ms=10, label="a")
    plt.xticks(rotation=45)
    a = copy.deepcopy(y)
    a.sort()
    plt.yticks(a)
    plt.xlabel("价格区间")
    plt.ylabel("销售数")
    plt.title("区间销售数")
    # upper left 将图例a显示到左上角
    plt.legend(loc="upper left")
    # 在折线图上显示具体数值, ha参数控制水平对齐方式, va控制垂直对齐方式
    for x1, y1 in zip(x, y):
        plt.text(x1, y1 + 1, str(y1), ha='center', va='bottom', fontsize=10, rotation=0)
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + os.sep + 'static' + os.sep + 'fenxi_img'
    if not os.path.exists(path):
        os.makedirs(path)
    paths = path + os.sep + 'zhexianxiaoshu.jpg'
    # plt.show()
    plt.savefig(paths, dpi=100)
    plt.close()



if __name__ == '__main__':
    danjia_section()
    bing_danjia()
    pinpai_section()
    bing_pinpai()
    chaping_to5()
    haoping_to5()
    zhexianyuling()
