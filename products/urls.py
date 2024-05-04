from django.urls import path
from .views import get_info, get_Phones, detail, add_Phones, update_Phones,delete_product


app_name = 'Phones'
urlpatterns = [
    path('', get_info, name='get_info'),
    path('products/<int:pk>', get_Phones, name='get_Phones'),
    path('products/detail/<int:pk>', detail, name='details'),
    path('add_products', add_Phones, name='add_Phones'),
    path('update/<int:pk>', update_Phones, name='update'),
    path('delete/<int:pk>', delete_product, name='delete_product'),
]