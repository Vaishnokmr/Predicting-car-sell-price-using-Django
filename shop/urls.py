from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='ShopeHome'),
    path('about/', views.about, name='AboutUs'),
    path('contact/', views.contact, name='ContactUs'),
    path('products/<int:myid>', views.productview, name='productview'),
    path('car/', views.car, name='SellCar'),
    path('car/result', views.result, name='result'),
    

    

]