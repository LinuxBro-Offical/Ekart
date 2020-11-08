from django.urls import path,include
from . import views

urlpatterns = [
    path('login', views.Login_view.as_view(),name="login"),
    path('home', views.Home_view.as_view(),name="home"),
    path('logout', views.LogoutView.as_view(),name="logout")
]