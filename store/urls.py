from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('login/',views.loginvw,name="login"),
    path('', views.home,name="home"),
    path('add_pr/',views.AddProductView.as_view(),name="add_pr"),
    path('add_pr_to_cart/<int:product_id>/',views.add_pr_to_cart,name="add_pr_to_cart"),
    path('add_pr_to_order/<int:product_id>/',views.add_pr_to_order,name="add_pr_to_order"),
    path('logout/', views.logout_vw,name="logout"),
    path('register/',views.register_vw,name="register"),
    path('cart/',views.see_cart,name="seecart"),
    path('search/',views.search,name="search"),
    path('dell_pr/<int:product_id>/',views.dell_product,name="deletepr"),
    path('dell/<int:pk>',views.DeleteproductView.as_view(),name="delbycbv"),
    path('upp/<int:pk>',views.UpdateproductView.as_view(),name='update')
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
