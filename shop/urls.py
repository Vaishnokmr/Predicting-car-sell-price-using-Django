from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/<int:myid>', views.productview, name='productview'),
    path('car/', views.car, name='SellCar'),
    path('car/result', views.result, name='result'),
    

    

]
