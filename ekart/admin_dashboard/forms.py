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
        }