import xadmin
from .models import *
from xadmin import views

class GlobalSettings(object):
    site_title = "Python商品销售数据分析系统"
    site_footer = "Python商品销售数据分析系统"
    menu_style = 'accordion'

class basesetting(object):
    enable_themes = True
    use_bootswatch = True

xadmin.site.register(views.CommAdminView,GlobalSettings)
xadmin.site.register(views.BaseAdminView,basesetting)
xadmin.site.register(XinXi)