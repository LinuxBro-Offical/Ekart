from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Home_view.as_view(),name="usersite_home"),
    path('products/', views.Product_view.as_view(),name="usersite_product"),
    path('products/details/', views.ProductDetailView.as_view(),name="product-details"),
    path('cart/', views.CartView.as_view(),name="cart"),
    path('register/', views.RegisterView.as_view(),name="register"),
    path('login/', views.LoginView.as_view(),name="login"),
    path('logout/', views.UserLogoutView.as_view(),name="user_logout")
]