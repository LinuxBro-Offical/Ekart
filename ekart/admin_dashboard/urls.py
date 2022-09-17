from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login_view.as_view(),name="login_admin"),
    path('home/', views.Home_view.as_view(),name="home"),
    path('logout', views.LogoutView.as_view(),name="logout"),
    path('category', views.Categoryview.as_view(),name="category"),
    path('subcategory', views.SubcategoryView.as_view(),name="subcategory"),
    path('brand', views.Brandview.as_view(),name="brand"),
    path('<pk>/category_delete/', views.CategoryDeleteView.as_view(),name='category_dlt'),
    path('<pk>/subcategory_delete/', views.SubcategoryDeleteView.as_view(),name='subcategory_dlt'),
    path('brand/validate', views.validate_brandname,name="brand_validate"),
    path('<pk>/brand_delete/', views.BrandDeleteView.as_view(),name='brand_dlt'),
    path('product', views.Productview.as_view(),name="product"),
    path('<pk>/product_delete/', views.ProductDeleteView.as_view(),name="product_dlt"),
    path('offer', views.Offerview.as_view(),name="offer"),
    path('<pk>/offer_delete/', views.OfferDeleteView.as_view(),name="offer_dlt"),
    path('seller', views.Sellerview.as_view(),name="seller"),
    path('<pk>/seller_delete/', views.SellerDeleteView.as_view(),name="seller_dlt"),
    path('order', views.Orderview.as_view(),name="order"),
    path('deals', views.DealsCreateView.as_view(), name="deals"),
    path('<pk>/deal_delete/', views.DealsDeleteView.as_view(),name="deal_dlt")
]
