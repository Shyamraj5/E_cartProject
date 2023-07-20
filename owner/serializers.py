from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User

class productSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"
    def validate(self, attrs):
        price=attrs.get("pr_price")
        if price<0:
            raise serializers.ValidationError("invalid price given ")
        return attrs


class UserSer(serializers.Serializer):
    class Meta:
        model=User
        fields=["username","password","email"]
        
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)