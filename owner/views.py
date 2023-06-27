from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import productSerializers
from rest_framework.response import Response
# Create your views here
class Productview(APIView):
    def post(self,request):
        ser=productSerializers(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"ok"})
        return Response({"msg":"faild"})
        