from django.urls import path
from . views import *

urlpatterns =[
    path("product",Productview.as_view(),name="pro"),
    
]