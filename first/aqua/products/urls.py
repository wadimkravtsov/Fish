from django.urls import path
from . import views
# from ..aqua.urls import urlpatterns

urlpatterns = [
    path('', views.aqua_base, name='aqua_base'),
    path('products/', views.products, name='products'),
    path('products/<int:category_id>/', views.products, name='category'),
    path('product/<int:pk>/', views.product, name='product'),
]