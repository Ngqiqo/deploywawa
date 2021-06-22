from django import forms
from .models import User

class Userform(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {
        "name" : forms.TextInput(attrs={"class": "form-control"}),
        "lastname" : forms.TextInput(attrs={"class": "form-control"}),
        "email" : forms.EmailInput(attrs={"class": "form-control"  }),
        "number" : forms.TextInput(attrs={"class": "form-control" }),
        "country" : forms.TextInput(attrs={"class": "form-control"  }),
        "city" : forms.TextInput(attrs={"class": "form-control"  }),
        
        }