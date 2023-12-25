from django.shortcuts import render,HttpResponse,reverse,redirect
from django.contrib.auth.decorators import login_required
from Electronics import models
from django.db.models import Q
from django.shortcuts import get_object_or_404,HttpResponseRedirect
import json
import random
# from .xietong import UserCf

# Create your views here.


@login_required
def index(request):
    if request.method == 'GET':
        datas = models.XinXi.objects.all().order_by('-id')[:10]
        return render(request,r"projects\table_s.html",locals())

@login_required
def user_profile(request):
    if request.method == 'GET':
        return render(request,'projects/user-profile.html',locals())

@login_required
def update_user(request):
    if request.method   == 'GET':
        data = models.Users.objects.get(username=request.user.username)
        return render(request,'projects/form_validations.html',locals())
    elif request.method == 'POST':
        datas = models.Users.objects.get(username=request.user.username)
        error = {}
        data = request.POST
        email = data.get('email','')
        if email != '' and '@' in str(email):
            email = email
        else:
            error['email'] = '邮箱格式错误'
        age = data.get('age','')
        try:
            int(age)
            if age != '' and 0 < int(age) and int(age) < 120:
                age = age
            else:
                raise Exception('年龄错误')
        except:
            error['age'] = '年龄错误'
        set = data.get('set','')
        if set != '' and str(set) in ['男','女']:
            set = set
        else:
            error['set'] = '性别格式错误'
        if error != {}:
            return render(request,'projects/form_validations.html',context={'data':datas,'error':error})
        else:
            models.Users.objects.filter(username=request.user.username).update(email=email,age=age,set=set)
            user = request.user
            return render(request, 'projects/user-profile.html', locals())



@login_required
def select_all(request):
    if request.method == 'POST':
        data = request.POST.get('projects_name', '')
        if data == '':
            datas = models.XinXi.objects.all().order_by('-id')[:10]
        elif data == 'all':
            datas = models.XinXi.objects.all()
        else:
            datas = models.XinXi.objects.filter(Q(name__icontains=data)|Q(shopname__icontains=data)|Q(pinpai__icontains=data)|Q(xinghao__icontains=data)).order_by('-count')
        return render(request,'projects/table_s.html',context={'datas':datas})

import os
import subprocess
@login_required
def spiders(request):
    if request.user.is_superuser:
        paths = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'spider.py'
        cmd = "python " + paths
        print(cmd)
        res = subprocess.Popen(cmd,shell=True)
        dicts = {
            "state": True,
            "content": "启动成功 ",
        }
        return HttpResponse(json.dumps(dicts))

@login_required
def fenxi(request):
    if request.method == 'GET':
        datas = models.XinXi.objects.all()
        num1 = len(models.XinXi.objects.filter(Q(price__gt=0) & Q(price__lte=1000)))
        num2 = len(models.XinXi.objects.filter(Q(price__gt=1000) & Q(price__lte=2000)))
        num3 = len(models.XinXi.objects.filter(Q(price__gt=2000) & Q(price__lte=3000)))
        num4 = len(models.XinXi.objects.filter(Q(price__gt=3000) & Q(price__lte=4000)))
        num5 = len(models.XinXi.objects.filter(Q(price__gt=4000) & Q(price__lte=100000)))
        chaping_datas = models.XinXi.objects.all().order_by('-chaping')[:5]
        haoping_datas = models.XinXi.objects.all().order_by('haoping')[:5]

        return render(request,'projects/fenxi.html',locals())

@login_required
def spiders1(request):
    if request.user.is_superuser:
        paths = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'fenxi.py'
        cmd = "python " + paths
        print(cmd)
        res = subprocess.Popen(cmd,shell=True)
        dicts = {
            "state": True,
            "content": "启动成功 ",
        }
        return HttpResponse(json.dumps(dicts))

@login_required
def item(request,id):
    if request.method == 'GET':
        data = get_object_or_404(models.XinXi,pk=id)

        datas = models.DianZan.objects.all()
        dicts = {}
        for dat1 in datas:
            if dicts.get(dat1.user.username, '') == '':
                dicts[dat1.user.username] = {}
                dicts[dat1.user.username][dat1.xinxi.id] = dat1.xinxi.avgScore
            else:
                dicts[dat1.user.username][dat1.xinxi.id] = dat1.xinxi.avgScore
        print(dicts)
        try:
            userCf = UserCf(data=dicts)
            recommandList=userCf.recomand(request.user.username, 2)
            # # print("最终推荐：%s"%recommandList)
            r = userCf.recommend(request.user.username)
            datas = []
            for rs in r:
                datas.append(get_object_or_404(models.XinXi,pk=rs[0]))
        except:
            datas = models.XinXi.objects.all().order_by('-avgScore')[:3]

        return render(request,'projects/detailed.html',locals())


@login_required
def dianzan(request,id):
    if request.method == 'GET':
        data = get_object_or_404(models.XinXi,pk=id)
        if not models.DianZan.objects.filter(Q(user=request.user)&Q(xinxi=data)):
            models.DianZan.objects.create(
                user=request.user,
                xinxi=data
            )
            dicts = {
                "state": True,
                "content": "点赞成功 ",
            }
        return HttpResponse(json.dumps(dicts))