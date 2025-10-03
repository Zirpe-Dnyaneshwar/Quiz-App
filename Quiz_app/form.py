from django import forms
from django.contrib.auth.models import User
class UserCreationForm(forms.ModelForm):
    
    username=forms.CharField(
        label="Enter Your Username",
        widget=forms.TextInput(
            attrs={
                'placeholder':'Username',
                'class': 'input-animate w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500'
            }
        )
    ) 
    password=forms.CharField(
        label="Enter Your Password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Password',
                'class': 'input-animate w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500'
            }
        )
    ) 
    confirm_password=forms.CharField(
        label="Comfirm Password ",
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Comfirm Password',
                'class': 'input-animate w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500'
            }
        )
    ) 
    class Meta:
        model=User
        fields=['username','password','confirm_password']


#=========================================================================
class Userloginform(forms.Form):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'class': 'w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-indigo-500 focus:outline-none'
            }
        )
    )
    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
                'class': 'w-full px-4 py-3 border rounded-lg focus:ring-2 focus:ring-indigo-500 focus:outline-none'
            }
        )
    )
 

#=========================================================================


