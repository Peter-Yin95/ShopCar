from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.ProductList),
    url(r'^(?P<IdNumber>\w+)/$', views.ProductDetails),
]