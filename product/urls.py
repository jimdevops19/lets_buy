from django.urls import path
from product import views

urlpatterns = [
    path("product/", views.product_view, name="product_view"),
]