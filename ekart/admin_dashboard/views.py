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

    template_name = 'index.html'
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
            if productform.is_valid() and imageform.is_valid():
                product = productform.save()
                product.images = imageform.save()
                brand.save()
                messages.success(request,"A new Product added")
                return redirect('brand')
            messages.error(request,"Form is not valid")
            return redirect('product')
        except:
            messages.error(request,"Can't read data")
            return redirect('product')


