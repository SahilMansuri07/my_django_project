from django import forms
from .models import Registeration,Course,Subject,Enrollment

class UserRegisteration(forms.ModelForm):
    class Meta:
        model = Registeration
        fields = ['name','email','password']
        widgets = {
            'name':forms.TextInput(),
            'email':forms.EmailInput(),
            'password':forms.PasswordInput(),
        }
        
        
class LoginChecking(forms.Form):
    email = forms.EmailField(label="Enter Email")
    password = forms.CharField(label="Enter Password",widget=forms.PasswordInput())



    
class AddCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']
        widgets = {
            'name':forms.TextInput()
        }
        
class AddSubject(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name']
        widgets = {
            'name':forms.TextInput()
        }