from django.shortcuts import render, HttpResponse ,redirect ,get_object_or_404 
from .models import Product, Cart,CartItem ,Category ,Order ,OrderItem
from django.http import HttpResponseForbidden 
from django.contrib.auth import logout ,login ,authenticate 
from users.models import CustomUser
from django.contrib.auth.decorators import login_required
from  users.forms import CustomRegisterForm
# Create your views here.

@login_required(login_url='/login/')
def home(request):
    product=Product.objects.all()
    return render(request, 'home.html',{"product":product})

def loginvw(request):
     if request.method=="POST":
         username=request.POST.get("username")
         password=request.POST.get("password")
         user=authenticate(request,username=username,password=password)
         if user is not None:
             login(request,user)
             return redirect("home")
         else:
             return render(request, "login.html", {"error": "❌ Username yoki parol noto‘g‘ri!"})
     return render(request,"login.html")


def add_product(request):  
    if not request.user.is_authenticated or request.user.role != "seller":
        return HttpResponseForbidden("Faqat seller mahsulot qo'sha oladi!")

    if request.method=="POST":
        product_title=request.POST.get("title")
        product_about=request.POST.get("about")
        pr_price=request.POST.get("price")
        pr_image=request.FILES.get("image")
        pr_stock=request.POST.get("stock")
        category_id=request.POST.get("category_id") 
        category=Category.objects.get(id=category_id)
        Product.objects.create(title=product_title,
                              about=product_about,
                              price=pr_price,
                              image=pr_image,stock=pr_stock,
                              category=category)
    return HttpResponse("Mahsulot qo'shildi")

def add_pr_to_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    cart,created=Cart.objects.get_or_create(user=request.user)

    cart_item ,created=CartItem.objects.get_or_create(cart=cart,product=product,defaults={"price":product.price , "quantity":1})
    if not created:
        cart_item.quantity+=1
        cart_item.save()

    return redirect("home")
    
def add_pr_to_order(request,product_id):
     product=Product.objects.get(id=product_id)
     order , created=Order.objects.get_or_create(user=request.user)

     order_item,created =OrderItem.objects.get_or_create(order=order,product=product,defaults={"price":product.price,"quantity":1})
     if not created :
        order_item.quantity+=1
        order_item.save()

     return redirect("home")

def dell_product(request,product_id):
    product=get_object_or_404(Product, id=product_id)
    if not request.user.seller and not hasattr(request.user, "seller"):
        return HttpResponseForbidden("Sizda bu mahsulotni o‘chirish huquqi yo‘q!")

    product.delete()

def logout_vw(request):
    logout(request)
    return redirect("login")

def register_vw(request):
    if request.method=="POST":
        form=CustomRegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect("home")
        
    else:
        form = CustomRegisterForm()
    return render(request, "register.html", {"form": form})

def see_cart(request):
    cart,created=Cart.objects.get_or_create(user=request.user)
    cart_u=CartItem.objects.filter(cart=cart)
    return render(request,'cart.html',{"cart_u":cart_u})

