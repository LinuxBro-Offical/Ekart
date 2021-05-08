from django.urls import path,include
from . import views
from django.conf.urls import url

urlpatterns = [
    path('login', views.Login_view.as_view(),name="login"),
    path('', views.Home_view.as_view(),name="home"),
    path('logout', views.LogoutView.as_view(),name="logout"),
    path('category', views.Categoryview.as_view(),name="category"),
    path('brand', views.Brandview.as_view(),name="brand"),
    path('<pk>/category_delete/', views.CategoryDeleteView.as_view(),name='category_dlt'),
    path('brand/validate', views.validate_brandname,name="brand_validate"),
    path('<pk>/brand_delete/', views.BrandDeleteView.as_view(),name='brand_dlt'),
    path('product', views.Productview.as_view(),name="product")

]
