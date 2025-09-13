from django.forms import BaseModelForm
from django.shortcuts import render, HttpResponse ,redirect ,get_object_or_404 ,get_list_or_404
from .models import Product, Cart,CartItem ,Category ,Order ,OrderItem 
from django.http import HttpResponseForbidden ,Http404
from django.contrib.auth import logout ,login ,authenticate 
from users.models import CustomUser
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin ,AccessMixin
from  users.forms import CustomRegisterForm
from django.views.generic import ListView,UpdateView, GenericViewError,DeleteView,CreateView 
from .forms import ProductForm
from django.urls import reverse_lazy
from typing import cast
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


from django.contrib.auth import get_user_model



class AddProductView(LoginRequiredMixin,CreateView):
    model=Product
    form_class=ProductForm
    template_name="addproduct.html"
    success_url=reverse_lazy("home")
    
    def form_valid(self, form):
        form.instance.seller=self.request.user
        return super().form_valid(form)
        

def add_pr_to_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    cart,created=Cart.objects.get_or_create(user=request.user)

    cart_item ,created=CartItem.objects.get_or_create(cart=cart,product=product,defaults={"price":product.price , "quantity":1})
    if not created:
        while cart_item.quantity < product.stock:
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

@login_required
def dell_product(request,product_id):
    product=get_object_or_404(Product, id=product_id)
    
    if product.seller != request.user:
       return HttpResponseForbidden("Sizda bu mahsulotni o‘chirish huquqi yo‘q!")

    product.delete()
    return redirect("home")

class DeleteproductView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
   model=Product
   template_name="delete.html"

   success_url=reverse_lazy("home")
    
   def test_func(self):
        pr = cast(Product,self.get_object())
        return self.request.user == pr.seller 
   

class UpdateproductView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
   model=Product
   template_name="updateproduct.html"
   fields=['title','image','price','about']
   success_url=reverse_lazy("home")
    
   def test_func(self):
        pr = cast(Product,self.get_object())
        if pr:
         return self.request.user == pr.seller 
        return Http404
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
    order,created=Order.objects.get_or_create(user=request.user)
    order_u=OrderItem.objects.filter(order=order)
   
    cart,created=Cart.objects.get_or_create(user=request.user)
    cart_u=CartItem.objects.filter(cart=cart)
    return render(request,'cart.html',{"cart_u":cart_u,"order_u":order_u})

def search(request):
     query=request.GET.get("q")
     if query :
        product=Product.objects.filter(title__icontains=query)
     else :
        product=Product.objects.all()
     return render(request , "home.html",{"product":product})