from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import IndexBanner

admin.site.site_title = '系统后台'
admin.site.site_header = '北京隐算科技管理后台'
admin.site.index_title = '后台主页'


# Register your models here.

@admin.register(IndexBanner)
class IndexBannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'banner_title', 'image_img')
    fields = ['banner_title','banner_brief','banner_img']


