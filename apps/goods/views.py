#from django.shortcuts import render

from .serializers import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from rest_framework import viewsets

from .models import Goods

# Create your views here.

# class GoodsListView(APIView):
#     def get(self, request, format=None):
#         goods = Goods.objects.all()[:10]
#         goods_serializer = GoodsSerializer(goods, many=True)
#         return Response(goods_serializer.data)

# class GoodsListView(mixins.ListModelMixin,generics.GenericAPIView ):
#     queryset = Goods.objects.all()[:10]
#     serializer_class = GoodsSerializer
#
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100

# class GoodsListView(generics.ListAPIView):
#     queryset = Goods.objects.all()
#     serializer_class = GoodsSerializer
#     pagination_class = GoodsPagination


class GoodsListViewSet(mixins.ListModelMixin,viewsets.GenericViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination

