from django.urls import path
from rest_framework.authtoken import views
from . views import *
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("product",ProductViewSet,basename="product")
router.register("user",SignupView,basename="userreg")
router.register("prodmv",ProductModelViewSet,basename="mv")

urlpatterns =[
    path("prod",Productview.as_view()),
    path('token',views.obtain_auth_token),
    
]+router.urls

#localhost/8000/owner/product/