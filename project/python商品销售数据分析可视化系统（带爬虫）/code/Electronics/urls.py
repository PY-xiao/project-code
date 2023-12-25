from django.conf.urls import url,include
from  . import views

app_name = 'lvguowang'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'user_profile/',views.user_profile,name='user_profile'),
    url(r'user_updata$', views.update_user, name='user_updata'),
    url(r'select_all$', views.select_all, name='select_all'),
    url(r'spiders$',views.spiders,name='spiders'),
    url(r'spfx$',views.spiders1,name='spiders1'),
    url(r'fenxi$',views.fenxi,name='fenxi'),
    url(r'item/([0-9]+)/', views.item, name='item'),
    url(r'dianzan/([0-9]+)/', views.dianzan, name='dianzan'),
]