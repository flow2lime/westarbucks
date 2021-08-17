from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

import json
from products.models import Menu, Category, Product

class ProductsView(View):
    def post(self,.request):
        data = json.loads(request.body)
        menu = Menu.objects.create(name=data['menu'])
        category = Category.objects.create(
            name = data['category'],
            menu = menu
            )
        Product.objects.create(
            name     = data['product'],
            category = category,
            menu     = menu
        )
        return HttpResponse({'MESSAGE': 'CREATED'}, status=201)
