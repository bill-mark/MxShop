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
    desc = models.CharField(default="",max_length=200,verbose_name="类别描述",help_text="类别描述")
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
    name = models.CharField(default="",max_length = 30,verbose_name="品牌名",help_text="品牌名")
    desc = models.CharField(default="",max_length = 200,verbose_name="品牌描述",help_text="品牌描述")
    image = models.ImageField(max_length=200,upload_to="brands/")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "品牌"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    category = models.ForeignKey(GoodsCategory,verbose_name="商品类目")
    good_sn = models.CharField(max_length=50,default="",verbose_name="商品唯一货号")
    name = models.CharField(max_length=100,verbose_name="商品名")
    click_num = models.IntegerField(default=0,verbose_name="点击数")
    sold_num = models.IntegerField(default=0,verbose_name="商品销售数量")
    fav_num = models.IntegerField(default=0,verbose_name="收藏数")
    goods_num = models.IntegerField(default=0,verbose_name="库存数")
    market_price = models.IntegerField(default=0,verbose_name="市场价格")
    shop_price = models.FloatField(default=0,verbose_name="本店价格")
    goods_brief = models.TextField(max_length=500,verbose_name="商品简短描述")
    goods_desc = UEditorField(verbose_name="内容",imagePath="goods/images/",width=1000,height=300,
                              filePath="goods/files/",default='')
    ship_free = models.BooleanField(default=True,verbose_name="是否承担运费")
    goods_front_image= models.ImageField(upload_to="",null=True,blank=True,verbose_name="封面图")
    is_new = models.BooleanField(default=False,verbose_name="是否新品")
    is_hot = models.BooleanField(default=False,verbose_name="是否热销")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsImage(models.Model):
    goods = models.ForeignKey(Goods,verbose_name="商品",related_name="images")
    images = models.ImageField(upload_to="",verbose_name="图片",null=True,blank=True)
    images_url = models.CharField(max_length=300,null=True,blank=True,verbose_name="图片URL")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品图片"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    goods = models.ForeignKey(Goods,verbose_name="商品")
    image = models.ImageField(upload_to='banner',verbose_name="轮播图片")
    index = models.IntegerField(default=0,verbose_name="轮播顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name="轮播商品"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name