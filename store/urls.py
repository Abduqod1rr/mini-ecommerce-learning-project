from django.urls import path 
from . import views

urlpatterns = [
    path('login/',views.loginvw,name="login"),
    path('', views.home,name="home"),
    path('add_pr/',views.add_product,name="add_pr"),
    path('add_pr_to_cart/<int:product_id>/',views.add_pr_to_cart,name="add_pr_to_cart"),
    path('add_pr_to_order/<int:product_id>/',views.add_pr_to_order,name="add_pr_to_order"),
    path('logout/', views.logout_vw,name="logout"),
    path('register/',views.register_vw,name="register"),
    path('cart/',views.see_cart,name="seecart"),
   
]
