from django import forms
from .models import *


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category

        fields=['name','description']
        widgets={
            'name':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter category a name"}),
            'description':forms.Textarea(attrs={'class': 'form-control','placeholder':'What this category is about ?',"rows":"5"})
        }

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand

        fields=['name','description']
        widgets={
            'name':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter a brand name"}),
            'description':forms.Textarea(attrs={'class': 'form-control','placeholder':'Brand description..',"rows":"5"})
        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image

        fields=['image']
        widgets={
            'image':forms.FileInput(attrs={'class':'custom-file-input', 'id':'customFile'})
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

        fields=['name','description','price','count','colours','specifications','categories','brand']
        widgets={
            'name':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Product name"}),
            'description':forms.Textarea(attrs={'class': 'form-control','placeholder':'Product description..',"rows":"5"}),
            'price':forms.NumberInput(attrs={'class':'form-control','placeholder':'Price'}),
            'count':forms.NumberInput(attrs={'class':'form-control','placeholder':'Number of products'}),
            'colours':forms.Select(attrs={'class': 'form-control'}),
            'categories':forms.Select(attrs={'class': 'form-control'}),
            'specifications':forms.Textarea(attrs={'class': 'form-control','placeholder':'Product specifications..',"rows":"5"}),
            'brand':forms.Select(attrs={'class': 'form-control'}),  
            'seller':forms.Select(attrs={'class': 'form-control'}),
            'offer':forms.Select(attrs={'class': 'form-control'})   
        }

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer

        fields=['title','offer_amount','percentage','start_date','end_date']
        widgets={
            'title':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Offer title"}),
            'product':forms.Select(attrs={'class': 'form-control'}),
            'brand':forms.Select(attrs={'class': 'form-control'}),
            'category':forms.Select(attrs={'class': 'form-control'}),
            'offer_amount':forms.NumberInput(attrs={'class':'form-control','placeholder':'Price'}),
            'percentage':forms.CheckboxInput,
            'start_date':forms.DateInput(attrs={'class':'form-control','placeholder':'YYYY-MM-DD'}),
            'end_date':forms.DateInput(attrs={'class':'form-control','placeholder':'YYYY-MM-DD'}),  
        }

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller

        fields=['name','number']
        widgets={
            'name':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Seller name"}),
            'number':forms.TextInput(attrs={"class":"form-control","placeholder":"xxxx xxxx xx"})  
        }
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address

        fields=['address_line1','address_line2','city','state','country','pincode']
        widgets={
            'address_line1':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Address"}),
            'address_line2':forms.TextInput(attrs={"class":"form-control","placeholder":"Enter Address line two"}),
            'city':forms.TextInput(attrs={"class":"form-control","placeholder":"City"}),
            'state':forms.TextInput(attrs={"class":"form-control","placeholder":"State"}),
            'country':forms.TextInput(attrs={"class":"form-control","placeholder":"Country"}),
            'pincode':forms.TextInput(attrs={"class":"form-control","placeholder":"Pin code"})        
        }