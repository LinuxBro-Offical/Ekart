from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Home_view.as_view(),name="usersite_home")
]