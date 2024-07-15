from user_site.models import Enduser
from django.views import View
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from .mixins import OTPMixin
from .models import Category, SubCategory

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer


# To Register New End User
class RegisterView(View, OTPMixin):

    def post(self, request):
        mobile = request.POST.get('mobile', None)
        otp = request.POST.get('otp', None)
        password = request.POST.get('password', None)
        user = Enduser.objects.filter(mobile=mobile)

        if not user and mobile and otp:
            if self.verify_otp(str(otp)):
                user = Enduser(mobile=mobile, password=password)
                user.set_password(user.password)
                user.save()
                return JsonResponse({"status": 201,
                                     "message": "User Account Created."})
            else:
                return JsonResponse({"status": 403,
                                     "message": "Incorrect OTP."})
        else:
            if user:
                return JsonResponse({"status": 400,
                                     "message": "User already exits."})
            else:
                self.generate_otp(mobile)
                return JsonResponse({"status": 200,
                                     "message": "OTP generated successfully."})


class LoginView(View, OTPMixin):

    def post(self, request):

        mobile = request.POST.get('mobile', '')
        password = request.POST.get('password', '')
        otp = request.POST.get('otp', '')
        print("Mobile:", mobile, "PASSWORD:", password, "OTP:", otp)
        if mobile and password:
            print("kitty")
            user = authenticate(request,
                                username=None, password=password,
                                mobile=mobile)
            print("USR:", user)
            if user is not None:
                login(request, user)
                print("LOGIN AYE")
                # Redirect to a success page.
                messages.success(request, "Login successfully")
                return JsonResponse({"status": 200,
                                     "message": "Login Success"})
            else:
                return JsonResponse({"status": 403,
                                     "message": "Invalid Credentials"})

        elif mobile and otp:
            user = Enduser.objects.get(mobile=mobile)

            if user is not None and self.verify_otp(otp):
                login(request, user)
                # Redirect to a success page.
                print("LOGIN AYE")
                messages.success(request, "Login successfully")
                return JsonResponse({"status": 200,
                                     "message": "Login Success"})
            else:
                return JsonResponse({"status": 403,
                                     "message": "Incorrect OTP"})

        elif mobile:
            user = Enduser.objects.filter(mobile=mobile)
            if user:
                self.generate_otp(mobile)
                return JsonResponse({"status": 200,
                                     "message": "OTP Generated"})
            else:
                return JsonResponse({"status": 404,
                                     "message": "Mobile number not registerd"})
        else:
            return JsonResponse({"status": 400,
                                 "message": "Mobile Number required"})


class UserLogoutView(RedirectView):
    url = '/'

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            logout(request)
            print("LOGOUT SUCCESS")
        return super(UserLogoutView, self).get(request, *args, **kwargs)


class Home_view(TemplateView):
    template_name = 'home.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):
        context = super(Home_view, self).get_context_data(**kwargs)
        context["category"] = Category.objects.all()
        context["subcategory"] = SubCategory.objects.all()
        return context


class LoginOtpView(TemplateView):
    pass


class Product_view(TemplateView):
    template_name = 'home/products.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):

        context = super(Product_view, self).get_context_data(**kwargs)
        return context


class ProductDetailView(TemplateView):
    template_name = 'home/detail.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):

        context = super(ProductDetailView, self).get_context_data(**kwargs)
        return context


class CartView(TemplateView):
    template_name = 'home/cart.html'
    login_url = 'login'

    def get_context_data(self, **kwargs):

        context = super(CartView, self).get_context_data(**kwargs)
        return context


class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            mobile = serializer.validated_data['mobile']
            password = serializer.validated_data['password']
            user = authenticate(request, mobile=mobile, password=password)
            if user is not None:
                login(request, user)
                return Response({'detail': 'Login successful'})
            else:
                return Response({'detail': 'Invalid mobile or password'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
