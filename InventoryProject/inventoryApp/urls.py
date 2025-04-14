from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create/', views.Product_create_view, name='product_create'),
    path('list/', views.Product_list_view, name='product_list'),
    path('update/<int:product_id>/', views.Product_update_view, name='product_update'),
    path('delete/<int:product_id>/', views.Product_delete_view, name='product_delete'),
]