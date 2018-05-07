# encoding:utf-8

from django.views.generic.base import View
from goods.models import Goods
from django.http import HttpResponse
import json

class GoodsListView_test(View):
    def get(self,request):
        json_list = []
        goods = Goods.objects.all()[0:10] #切片操作 取前十个数 0可以省略

        for good in goods:
            json_dict = {}
            json_dict["name"] = good.name
            json_dict["category"] = good.category.name
            json_dict["market_price"] = good.market_price
            json_list.append(json_dict)

        return  HttpResponse(json.dumps(json_list),content_type="application/json")


        # from django.forms.models import model_to_dict
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)


        # from django.core import serializers
        # json_data = serializers.serialize("json",goods)
        # json_data = json.loads(json_data)
        # from django.http import JsonResponse
        # return JsonResponse(json_data,safe=False)