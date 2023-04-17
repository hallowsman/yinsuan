from django.db import models
from django.utils.html import format_html


# Create your models here.

class IndexBanner(models.Model):
    banner_title = models.CharField('大图标题', max_length=20)  # 标题
    banner_brief = models.CharField('大图描述', max_length=100)  # 简介
    banner_img = models.ImageField('大图图片', upload_to='')  # 图片
    # banner_img = StdImageField(upload_to='static/media')
    isDelete = models.BooleanField('物理删除', default=False)  # 是否删除

    class Meta:
        db_table = 'indexbanner'
        verbose_name_plural = "首页大图"
        verbose_name = "大图"

        # 列表页显示图片
    def image_img(self):
        if not self.banner_img:
            return '无'
        else:
            return format_html(
                """<div><img src='{}' style='width:50px;height:50px;' ></div>""",
                self.banner_img.url)






