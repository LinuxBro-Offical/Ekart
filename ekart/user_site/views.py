from django.shortcuts import render,redirect
from django.views.generic import TemplateView ,RedirectView
# from .forms import *  
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
# Create your views here.




class Home_view(TemplateView):

    template_name = 'home.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):

        context = super(Home_view, self).get_context_data(**kwargs)
        return context