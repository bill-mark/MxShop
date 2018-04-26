# encoding:utf-8
from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField
# Create your models here.


class GoodsCategory(models.Model):
    "商品类别"
    CATEGORY_TYPE = (
        (1,"一级类目"),
        (2,"二级类目"),
        (3,"三级类目")
    )

    name = models.CharField(default="",max_length=30,verbose_name="类别名",help_text="类别名")
    code = models.CharField(default="",max_length=30,verbose_name="类别code",help_text="类别code")
    desc = models.CharField(default="",verbose_name="类别描述",help_text="类别描述")
    category_type = models.IntegerField(choices=CATEGORY_TYPE,verbose_name="类目级别",help_text="类目级别")
    parent_category = models.ForeignKey("self",null=True,blank=True,verbose_name="父类目录",help_text="父类目录",
                                        related_name="sub_cat")
    is_tab= models.BooleanField(default=False,verbose_name="是否导航",help_text="是否导航")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsCategoryBand(models.Model):
    name = models.CharField(default="",max_length=30,verbose_name="品牌名",help_text="品牌名")
    desc = models.TextField(default="",max_length=200,verbose_name="品牌描述",help_text="品牌描述")
    image = models.IntegerField(max_length=200,upload_to="brand/images/")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "品牌"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    category = models.ForeignKey(GoodsCategory,null=True,blank=True,verbose_name="商品类目")
    good_sn = models.CharField(max_length=50,default="",verbose_name="商品唯一货号")
    name = models.CharField(max_length=300,)
    click_num = models.IntegerField()
    sold_num = models.IntegerField()
    fav_num = models.IntegerField()
    goods_num = models.IntegerField()
    market_price = models.IntegerField()
    shop_price = models.FloatField()
    goods_brief = models.TextField()
    goods_desc = UEditorField()
    ship_free = models.BooleanField()
    is_new = models.BooleanField(default=False)
    is_hot = models.BooleanField(default=False)

    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")


class GoodsImage(models.Model):
    goods = models.ForeignKey(Goods)
    images = models.ImageField()
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name