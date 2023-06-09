from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django . views.generic import View,TemplateView,CreateView,ListView,DetailView
from .forms import*
from django. urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages
from owner.models import Product
from .models import Cart
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
# Create your views here.
def signin_required(fn):
    def inner(request,*args, **kwargs):
        if request.user.is_authenticated:
            return fn(request,*args, **kwargs)
        else:
            messages.error(request,"please login first")
            return redirect("signin")
    return inner
dec=[signin_required,never_cache]

@method_decorator(dec,name='dispatch')
class Home(ListView):
    template_name="home.html"
    model=Product
    context_object_name="product"
    

    


# class signUP(View):
#     def get(self,request,*args, **kwargs):
#         form=signUpform()
#         return render(request,"signUp.html",{"form":form})
#     def post(self,request,*args, **kwargs):
#         form_data=signUpform(data=request.POST)
#         if form_data.is_valid():
#             form_data.save()
#             return redirect('home')
#         else:
#             return render(request,"signUp.html",{"form":form_data})
class signUP(CreateView):
    template_name="signUp.html"
    form_class=signUpform
    model=User
    success_url=reverse_lazy('signin')
    def form_valid(self,form):

        messages.success(self.request,"registration successfull")
        print("vaid")
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.error(self.request,"registraton error")
        print("invalid")
        return super().form_invalid(form)
    
class signIn(View):
    def get(self,request,*args, **kwargs):
        form=signInform()
        return render(request,"signIn.html",{"form":form})
    def post(self,request,*args, **kwargs):
        form_data=signInform(data=request.POST,files=request.FILES)
        if form_data.is_valid():
            uname=form_data.cleaned_data.get("username")
            password=form_data.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=password)
            if user:
                login(request,user)
                return redirect("home")
            else:
                return render(request,"signUp.html",{'form_data':form_data})
        
        else:
            return render(request,"signUp.html",{'form_data':form_data})
        
# class Seemore(ListView):
#     def get(self,request,*args, **kwargs):
#         pr=Product.objects.all()
#         return render(request,"seemore.html",{'product':pr})


# class ProductList(ListView):
#      def get( self,request,*args, **kwargs):
#         id=kwargs.get('id')
#         product = Product.objects.filter(id=id)
#         return render(request, 'seemore.html', {'product': product})

@method_decorator(dec,name='dispatch')
class productDet(DetailView):
    template_name="seemore.html"
    model=Product
    context_object_name="product"
    pk_url_kwarg='id'


@method_decorator(dec,name='dispatch')
class MyCart(TemplateView):
    template_name='Mycart.html'
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["cart"]=Cart.objects.filter(user=self.request.user)
        
        return context
    
   
dec
def Delcart(request,*args,**kwargs):
        id=kwargs.get("id")
        Cart.objects.filter(id=id).delete()
        messages.success(request,"item removed")
        return redirect("mycart")
dec    
def addcart(request,*args,**kwargs):
    id=kwargs.get("id")
    product=Product.objects.get(id=id)
    user=request.user
    if Cart.objects.filter(product=product,user=request.user):
        messages.warning(request,"Already Added in Cart")
        return redirect('home')
    else:
        Cart.objects.create(product=product,user=user,status="carted")
        messages.success(request,"Added to Cart")
        return render(request,"Mycart.html")
    

# class totel(TemplateView):
#     template_name=""
#     def cart_view(request,*args,**kwargs):
#      id=kwargs.get("id")
def cart_view(request):
    cart = Cart.objects.get(id=1)  # Replace 1 with the actual cart ID
    total_price = cart.calculate_total_price()

    return render(request, 'Mycart.html', {'cart': cart, 'total_price': total_price})
    
   