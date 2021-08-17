from django.urls import path
from products.views import ProductsView

urlpatters = [
    path('', ProductsView.as_view()),
]