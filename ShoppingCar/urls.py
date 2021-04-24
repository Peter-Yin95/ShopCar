from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.MyCar),
    url(r'^BuyNow/$',views.BuyNow)
]