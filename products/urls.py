from django.urls import path
from .views import *

app_name="products"


urlpatterns = [
   path('profile/',product_profile,name="p-profile"),
   path("update/<int:id>/",update_data,name='p-update'),
   path('remove/<int:id>/',remove_data,name='p-remove'),
   path('dashboard/',dashboard,name='p-dashboard'),
   path("product-details/<int:id>/",product_details,name="p-products"),
]
