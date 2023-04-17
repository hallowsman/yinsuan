from django.urls import path, re_path
from django.views.static import serve

from yinsuan import settings
from . import views

urlpatterns = [
    path('', views.index),  # 主页
    re_path(r'^index/$', views.index),
    re_path(r'^index123/$', views.index),
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
]
