# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-26 09:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_auto_20180426_0837'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsCategoryBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='品牌名', max_length=30, verbose_name='品牌名')),
                ('desc', models.CharField(default='', help_text='品牌描述', max_length=200, verbose_name='品牌描述')),
                ('image', models.ImageField(max_length=200, upload_to='brands/')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsCategory', verbose_name='商品类目')),
            ],
            options={
                'verbose_name': '品牌',
                'verbose_name_plural': '品牌',
            },
        ),
        migrations.CreateModel(
            name='HotSearchWords',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.CharField(default='', max_length=20, verbose_name='热搜词')),
                ('index', models.IntegerField(default=0, verbose_name='排序')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '热搜词',
                'verbose_name_plural': '热搜词',
            },
        ),
        migrations.CreateModel(
            name='IndexAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='goods.GoodsCategory', verbose_name='商品类目')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goods', to='goods.Goods')),
            ],
            options={
                'verbose_name': '首页商品类别广告',
                'verbose_name_plural': '首页商品类别广告',
            },
        ),
        migrations.DeleteModel(
            name='GoodsCategoryBand',
        ),
    ]
