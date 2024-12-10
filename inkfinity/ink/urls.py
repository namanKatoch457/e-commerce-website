from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.urls import include

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="aboutus"),
    path('contact/',views.contact_view,name="contactus"),
    path('tracker/',views.tracker,name="tracker"),
    path('products/<int:id>',views.prodView,name="productview"),
    path('checkout/',views.checkout,name="checkout"),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('cart/delete/<int:item_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('cart/checkout/', views.checkout_view, name='checkout'),
    path('cart/checkout/order_summary',views.order_summary,name='order_summary'),
    path('cart/', views.cart_view, name='cart'),
]


