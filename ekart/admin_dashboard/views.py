from django.shortcuts import render,redirect
from django.views.generic import TemplateView ,RedirectView
# from .forms import *  
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import *
from .forms import *
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

class Categoryview(LoginRequiredMixin,TemplateView):
    template_name = 'categories.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(Categoryview, self).get_context_data(**kwargs)
        categories = Category.objects.all()
        context["categories"] = categories
        context["form"] = CategoryForm
        return context

