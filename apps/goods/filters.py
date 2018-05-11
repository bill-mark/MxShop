# encoding:utf-8


import django_filters
from django_filters import rest_framework as filters
from django.db.models import Q
from .models import Goods


class GoodsFilter(filters.FilterSet):
    "商品过滤类"
    price_min = filters.NumberFilter(name='shop_price',lookup_expr='gte')
    price_max = filters.NumberFilter(name='shop_price', lookup_expr='lte')
    top_category = filters.NumberFilter(method='top_category_filter')

    #查找第一类别下面所属商品
    def top_category_filter(self,queryset,name,value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['price_min','price_max']
