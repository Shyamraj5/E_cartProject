from django.urls import path
from .views import *



urlpatterns =[
    path('signin',signIn.as_view(),name="signin"),
    path('',Home.as_view(),name='home'),
    path("seemore/<int:id>",productDet.as_view(),name="see"),
    path("addcart/<int:id>",addcart,name="addcart"),
    path("mycart",MyCart.as_view(),name="mycart"),
    path('delcart/<int:id>',Delcart,name="delcart")

]