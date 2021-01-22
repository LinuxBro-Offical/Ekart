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