from . models import Cart

def count(request):
    if request.user.is_authenticated:
        cnt=Cart.objects.filter(user=request.user).count()
        return{"count":cnt}
    else:
        return{"count":0}