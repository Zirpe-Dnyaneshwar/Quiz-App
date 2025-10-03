from django import forms
from django.contrib.auth.models import User
class UserCreationForm(forms.ModelForm):
    
    username=forms.CharField(
        label="Enter Your Username",
        widget=forms.TextInput(
            attrs={
                'placeholder':'Username',
                'class':'form-control '
            }
        )
    ) 
    password=forms.CharField(
        label="Enter Your Password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Password',
                'class':'form-control '
            }
        )
    ) 
    confirm_password=forms.CharField(
        label="Comfirm Password ",
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Comfirm Password',
                'class':'form-control '
            }
        )
    ) 
    class Meta:
        model=User
        fields=['username','password','confirm_password']


#=========================================================================
class Userloginform(forms.Form):
    username=forms.CharField(
        label="Enter Your Username",
        widget=forms.TextInput(
            attrs={
                'placeholder':'Username',
                'class':'form-control mb-4'
            }
        )
    ) 
    password=forms.CharField(
        label="Enter Your password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Password',
                'class':'form-control mb-4'
            }
        )
    )     

#=========================================================================


