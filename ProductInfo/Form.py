from  django import forms
from django.forms import ModelForm
from .models import ProductDetail
#显示产品信息
class ProductDetailForm(ModelForm):
    class Meta:
        model=ProductDetail
        fields='__all__'
