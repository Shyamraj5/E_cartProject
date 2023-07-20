from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import productSerializers,UserSer
from rest_framework.response import Response
from . models import Product
from rest_framework.viewsets import ViewSet,ModelViewSet
from django . contrib. auth. models import User
from rest_framework . decorators import action
from rest_framework import authentication,permissions
# Create your views here
class Productview(APIView):
    def get(self,request):
        prod=Product.objects.all()
        dish=productSerializers(prod,many=True)
        return Response(data=dish.data)
    def post(self,request):
        ser=productSerializers(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"ok"})
        return Response({"msg":"faild"})
    
class ProductViewSet(ViewSet):
    def list(self,):
        prod=Product.objects.all()
        ser=productSerializers(prod,many=True)
        return Response(data=ser.data)
    def retreve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        prod=Product.objects.all(id=id)
        ser=productSerializers(prod)     
        return Response(data=ser.data)
    def create(self,request):
        ser=productSerializers(data=request.data,many=True)
        if ser.is_valid():
            ser.save()
            return Response(data=ser.data)
        return Response(data=ser.errors)
    def update(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        prod=Product.objects.get(id=id)
        ser=productSerializers(data=request.data,instance=prod)
        if ser.is_valid():
            ser.save()
            return Response(data=ser.data)
        return Response(data=ser.errors)
    def distroy(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Product.objects.filter(id=id).delete()
        return Response({"msg":"delte"})
    

    #custom methode
    @action(methods="GET",detail=False)
    def category(self):
        cat=Product.objects.values_list("category").distinct()
        return Response(data=cat)


class ProductModelViewSet(ModelViewSet):
    serializer_class=productSerializers
    queryset=Product.objects.all()
    authentication_classes=[authentication.TokenAuthentication,]
    permission_classes=[permissions.IsAuthenticated]

class SignupView(ViewSet):
    # def list(self):
    #     user=User.objects.all()
    #     ser=productSerializers(user,many=True)
    #     return Response(data=ser.data)
    def create(self,request,*args,**kwargs):
        ser=UserSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"success"})
        return Response(data=ser.errors)
    



    
    
        