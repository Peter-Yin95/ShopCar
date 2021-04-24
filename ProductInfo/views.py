from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.

def ProductList(request):
    return HttpResponse("TEST")

from .Form import ProductDetailForm
from .models import ProductDetail
from ShoppingCar.models import MyCars
def ProductDetails(request,IdNumber):
    if request.method=='POST':
        if 'Creat' in request.POST:#新建商品
            if ProductDetail.objects.filter(ProductID=request.POST['ProductID'][0:4]):
                return HttpResponseRedirect('/ProductList/%s/' % str(request.POST['ProductID']+'C'))
            else:
                NewProduct = ProductDetailForm(request.POST)
                if NewProduct.is_valid():
                    SaveNew=NewProduct.save(commit=False)
                    SaveNew.ProductID=request.POST['ProductID'][0:4]
                    SaveNew.save()
                    return HttpResponseRedirect('/ProductList/%s/' % str(request.POST['ProductID']+'E'))
        elif 'Modify' in request.POST:#修改商品
            ProductDetail.objects.filter(ProductID=request.POST['ProductID'][0:4]).update(ProductName=request.POST['ProductName'],
                                                                    ProductPrice=request.POST['ProductPrice'],
                                                                    ProductNumber=request.POST['ProductNumber'],
                                                                    ProductOffer=request.POST['ProductOffer'])
            return HttpResponseRedirect('/ProductList/%s/' % str(request.POST['ProductID']+'M'))
        elif 'AddCar' in request.POST:#加入购物车
            InputCar=MyCars.objects.create(ProductID=request.POST['ProductID'][0:4],
                                           ProductName=request.POST['ProductName'],
                                           ProductPrice=request.POST['ProductPrice'])
            InputCar.save()
            return HttpResponseRedirect('/ProductList/%s/' % str(request.POST['ProductID'] + 'A'))
        elif 'BuyNow'in request.POST:#立即购买
            request.session['ProductID'] = request.POST['ProductID'][0:4]
            request.session['ProductName'] = request.POST['ProductName']
            request.session['ProductPrice'] = request.POST['ProductPrice']
            return HttpResponseRedirect('/MyCar/BuyNow/')
        else:#我的购物车
            return HttpResponseRedirect('/MyCar/')

    else:
        if IdNumber[-1]=='C':
            types='已存在'
        elif IdNumber[-1]=='E':
            types='已新增'
        elif IdNumber[-1]=='A':
            types='已加入购物车'
        elif IdNumber[-1]=='M':
            types='已修改'
        else:
            types = ''
        formValue=ProductDetail.objects.filter(ProductID=IdNumber[0:4])[0]
        formValue=ProductDetailForm({'ProductID':IdNumber[0:4],'ProductName':formValue.ProductName,
                                     'ProductPrice':formValue.ProductPrice,'ProductNumber':
                                         formValue.ProductNumber,'ProductOffer':formValue.ProductOffer})
        return render(request,'ProductDetail.html',{'form':formValue,'types':types})

