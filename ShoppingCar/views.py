from django.shortcuts import render
# Create your views here.
from .models import MyCars
def MyCar(request):
    ProductList=[]
    ProductOne={}
    Ap=MyCars.objects.filter()
    for item in Ap:
        ProductOne['ProductName']=item.ProductName
        ProductOne['ProductPrice']=item.ProductPrice
        ProductList.append(ProductOne)
        ProductOne={}
    return render(request,'MyCarHtml.html',{'ProductList':ProductList})

def BuyNow(request):
    ProductList = []
    ProductOne = {}
    ProductOne['ProductName'] = request.session.get('ProductName')
    ProductOne['ProductPrice'] = request.session.get('ProductPrice')
    ProductList.append(ProductOne)
    return render(request, 'MyCarHtml.html', {'ProductList': ProductList})