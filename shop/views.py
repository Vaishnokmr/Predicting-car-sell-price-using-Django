from django.shortcuts import render
from shop.models import Product
from math import ceil
import pickle
import numpy as np
# Create your views here.
from django.http import HttpResponse

model=pickle.load(open('random_forest_regression_model.pkl','rb'))


def index(request):
    products = Product.objects.all()
    n = len(products)
    nslide = n//4 + ceil((n/4)-(n//4))
    params = {"No_of_slides" : nslide , 'range' : range(1,nslide) , 'product' : products}
    #allProds=[[products, range(1, n), nslide],[products, range(1, n), nslide],]
    #params = {"allProds" : allProds}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return render(request,'shop/contact.html')

def productview(request,myid):
    product=Product.objects.filter(id=myid)
    
    #fetch product fromid 
    return render(request,'shop/productview.html',{'product':product[0]})

def car(request):
    return render(request,'shop/car.html')


    
def result(request):

    
    Fuel_Type_Diesel=0  
    
    Present_Price=float(request.GET['Present_Price'])
    Kms_Driven = int(request.GET['Kms_Driven'])
    Owner = int(request.GET['Owner'])
    Old_Car =  int(request.GET['Old_Car'])
    Price_rate_change =  float(request.GET['Price_rate_change'])
    Fuel_Type_Petrol = request.GET['Fuel_Type_Petrol']
    Fuel_Type_Petrol=request.GET['Fuel_Type_Petrol']
    if(Fuel_Type_Petrol=='Petrol'):
        Fuel_Type_Petrol=1
        Fuel_Type_Diesel=0
    else:

        Fuel_Type_Petrol=0
        Fuel_Type_Diesel=1    
    
    Seller_Type_Individual=request.GET['Seller_Type_Individual']
    if(Seller_Type_Individual=='Individual'):
        Seller_Type_Individual=1
    else:
        Seller_Type_Individual=0
    Transmission_Manual=request.GET['Transmission_Manual']
    if(Transmission_Manual=='Mannual'):
        Transmission_Manual=1
    else:
        Transmission_Manual=0
    
    prediction=model.predict(np.array([[Present_Price,Kms_Driven,Owner,Old_Car,Price_rate_change,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Manual]]))
    output=round(prediction[0],2)
   
    price = "You Can Sell your Car at "+ u"\u20B9" + str(output) + "L"
    if Present_Price<0:
        return render(request, "shop/car.html",{'prediction_texts' : "Sorry you cannot sell this car"})
    else:
        return render(request, 'shop/car.html',{'prediction_text' : price})
    




    
    

