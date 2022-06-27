from django.urls import re_path
from product1 import views
urlpatterns = [
    re_path(r'^products/$', views.product_list),
    re_path(r'^products/(?P<pk>[0-9]+)/$', views.product_detail),
]