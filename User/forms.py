from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm ,UserChangeForm
from .models import *

#user-signup-form
class sign_up_form(UserCreationForm):
    password1 = forms.CharField(label="Password",max_length=50,widget=forms.PasswordInput(attrs={'placeholder':"Enter your password"}))
    password2 = forms.CharField(label="Password Again",max_length=50,widget=forms.PasswordInput(attrs={'placeholder':"Enter your password again"}))
    class Meta:
        model = User
        fields = ['username',"first_name","last_name","email"]
        widgets= {
            "username" : forms.TextInput(attrs={"placeholder" : "Enter Your Username"}),
            "first_name" : forms.TextInput(attrs={"placeholder" : "Enter Your First Name"}),
            "last_name" : forms.TextInput(attrs={"placeholder" : "Enter Your Last Name"}),
            "email" : forms.EmailInput(attrs={"placeholder" : "Enter Your Email_Id",})
        }



class profile_form_superuser(UserChangeForm):
    password= None
    class Meta:
        model = User
        exclude=['password','groups',"user_permissions"]

class profile_form_user(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        # fields = "__all__"


#user_Form
class userform(forms.ModelForm):
    username=forms.CharField(max_length=150,disabled=True,widget=forms.TextInput())
    first_name=forms.CharField(max_length=150,widget=forms.TextInput())
    last_name=forms.CharField(max_length=150,widget=forms.TextInput())
    email=forms.EmailField(disabled=True,widget=forms.EmailInput())
    class Meta:
        model=User
        fields=["username","first_name","last_name","email"]



#User_profile_form
class user_profile_form(forms.ModelForm):
    class Meta:
        model=User_profile_model
        exclude=['user']
        labels={
            "user_address":"Address",
            "user_contact_no":"Contact_No",
            "user_age":"Age",
            "user_gender":"Gender"
        }
        widgets={
            "user_address":forms.Textarea(attrs={"placeholder":"Enter Your Address"}),
            "user_contact_no":forms.NumberInput(attrs={"placeholder":"Enter Your Contact_No"}),
            "user_age":forms.NumberInput(attrs={"placeholder":"Enter Your Age"}),
            "user_gender":forms.Select(),
            "user_profile_pic":forms.FileInput()
        }

    def clean_user_contact_no(self):
        data = self.cleaned_data["user_contact_no"]
        if len(str(data)) !=10:
          raise forms.ValidationError("Enter 10 Digit Mobile Number")
        return data


#Email Verification Form
class user_verify_email_form(UserCreationForm):
    password1=None
    password2=None
    class Meta:
        model=User
        fields=['email']
        widgets={"email" : forms.EmailInput(attrs={
            "required": True,
            "placeholder": "Enter Your Email"
        })}


#Otp Verification Form
class user_otp_verify_form(forms.ModelForm):
    class Meta:
        model= otp
        fields="__all__"

#Email Verification Form

class email_verify_form(UserCreationForm):
    password1=None
    password2=None
    class Meta:
        model=User
        fields=['email']
        widgets={"email" : forms.EmailInput(attrs={
            "required": True,
            "placeholder": "Enter Your Email"
        })}