from django.shortcuts import render,redirect
from django.views.generic import TemplateView, RedirectView
from django.views.generic.edit import DeleteView 
# from .forms import *  
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import *
from .forms import *
from django.http import JsonResponse
import json
from django.core import serializers
import datetime


# Create your views here.

class Login_view(TemplateView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('login')
        else:
            context = super(Login_view, self).dispatch(request, *args, **kwargs)
        return context

    def post(self,request):

        username = request.POST.get('username','')
        password = request.POST.get('password','')
        next_url = request.POST['next']
        if username and password:
            user = authenticate(request, username=username, password=password)

            if user is not None and user.is_superuser:
                login(request, user)
                # Redirect to a success page.
                if next_url != "":
                    return redirect(next_url)
                return redirect('home')
            else:
                messages.error(request,"Invalid Credentials")
                return redirect('login')
        else:
            messages.error(request,"Username And Password Required")
            return redirect('login')
            
class LogoutView(RedirectView):
    
    url = 'login'

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            logout(request)
        
        return super(LogoutView, self).get(request, *args, **kwargs)

class Home_view(LoginRequiredMixin,TemplateView):

    template_name = 'reports.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):

        context = super(Home_view, self).get_context_data(**kwargs)
        return context

# Category
class Categoryview(LoginRequiredMixin,TemplateView):
    template_name = 'categories.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(Categoryview, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        context["categories"] = categories
        context["form"] = CategoryForm
        return context
    def post(self,request):
        try:
            categoryform = CategoryForm(request.POST or None)
            if categoryform.is_valid():
                categoryform.save()
                messages.success(request,"Category created successfully")
                return redirect('categories')
            return JsonResponse({"status":403,"message":"Category name is already taken"})
        except:
            return JsonResponse({"status":404, "message":"Data not recived"})
    
class CategoryDeleteView(RedirectView): 
    url = '/admin/category'

    def get(self,request,*args,**kwargs):
        category = Category.objects.get(pk=kwargs["pk"])
        category.delete()
        messages.error(request,"Category Deleted")
        return super(CategoryDeleteView, self).get(request, *args, **kwargs)

#Brand
class Brandview(LoginRequiredMixin,TemplateView):
    template_name = 'brands.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(Brandview, self).get_context_data(**kwargs)
        brands = Brand.objects.all()
        context["brands"] = brands
        context["form"] = BrandForm
        context["imageform"] = ImageForm
        return context
    def post(self,request):
        try:
            brandform = BrandForm(request.POST or None)
            imageform = ImageForm(request.POST,request.FILES or None)
            if brandform.is_valid() and imageform.is_valid():
                brand = brandform.save()
                brand.logo = imageform.save()
                brand.save()
                messages.success(request,"A new brand added")
                return redirect('brand')
            messages.error(request,"Form is not valid")
            return redirect('brand')
        except:
            messages.error(request,"Can't read data")
            return redirect('brand')

def validate_brandname(request):
    try:
        brandname = request.POST.get("name", None)
        print(brandname)
        brand = Brand.objects.filter(name = brandname) 
        if brand[0].name == brandname :
            return JsonResponse({"status":403,"message":"Brand with same name already exists"})
    except:
            return JsonResponse({"status":404, "message":"Valid name"})

class BrandDeleteView(RedirectView): 
    url = '/admin/brand'

    def get(self,request,*args,**kwargs):
        brand = Brand.objects.get(pk=kwargs["pk"])
        brand.delete()
        messages.error(request,"Brand Deleted")
        return super(BrandDeleteView, self).get(request, *args, **kwargs)

#Product
class Productview(LoginRequiredMixin,TemplateView):
    template_name = 'products.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(Productview, self).get_context_data(**kwargs)
        products = Product.objects.all()
        context["products"] = products
        context["form"] = ProductForm
        context["imageform"] = ImageForm
        return context
    def post(self,request):
        try:
            productform = ProductForm(request.POST or None)
            imageform = ImageForm(request.POST,request.FILES or None)
            print("valid ahno:",productform.is_valid())
            print('form error',productform.errors)
            if productform.is_valid() and imageform.is_valid():
                product = productform.save()
                product.images.add(imageform.save())
                product.save()
                messages.success(request,"A new Product added")
                return redirect('product')
            messages.error(request,"Form not valid")
            return redirect('product')
        except:
            messages.error(request,"Can't read data")
            return redirect('product')

class ProductDeleteView(DeleteView):
    model = Product
    success_url ="/admin/product"

    def delete(self, request, *args, **kwargs):
        messages.success(request,"Product deleted successfully")   
        return super().delete(request, *args, **kwargs)

#Offer
class Offerview(LoginRequiredMixin,TemplateView):
    template_name = 'offer.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(Offerview, self).get_context_data(**kwargs)
        offers = Offer.objects.all()
        context["offer"] = offers
        context["datenow"] = datetime.date.today()
        context["form"] = OfferForm
        return context
    def post(self,request):
        try:
            offerform = OfferForm(request.POST or None)
            print('form error',offerform.errors)
            print("form valid ahnu",offerform.is_valid())
            if offerform.is_valid():
                offerform.save()
                messages.success(request,"New Offer Created")
                return redirect('offer')
            messages.error(request,"Form not valid")
            return redirect('offer')
        except:
            messages.error(request,"Can't read data")
            return redirect('offer')

class OfferDeleteView(DeleteView):
    model = Offer
    success_url ="/admin/offer"

    def delete(self, request, *args, **kwargs):
        messages.success(request,"Offer deleted successfully")   
        return super().delete(request, *args, **kwargs)

#Seller
class Sellerview(LoginRequiredMixin,TemplateView):
    template_name = 'seller.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(Sellerview, self).get_context_data(**kwargs)
        sellers = Seller.objects.all()
        context["seller"] = sellers
        context["form"] = SellerForm
        context["addressform"] = AddressForm
        return context
    def post(self,request):
        try:
            sellerform = SellerForm(request.POST or None)
            addressform = AddressForm(request.POST or None)
            if sellerform.is_valid() and addressform.is_valid():
                seller = sellerform.save()
                seller.address = addressform.save()
                seller.save()
                messages.success(request,"New Seller added")
                return redirect('seller')
            messages.error(request,"Form not valid")
            return redirect('seller')
        except:
            messages.error(request,"Can't read data")
            return redirect('seller')

class SellerDeleteView(DeleteView):
    model = Seller
    success_url ="/admin/seller"

    def delete(self, request, *args, **kwargs):
        messages.success(request,"Seller deleted successfully")   
        return super().delete(request, *args, **kwargs)

class Orderview(LoginRequiredMixin,TemplateView):
    template_name = 'order.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(Orderview, self).get_context_data(**kwargs)
        orders = Order.objects.all()
        context["order"] = orders
        return context