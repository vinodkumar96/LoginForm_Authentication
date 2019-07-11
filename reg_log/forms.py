from django import forms
from . models import Reg
class Reg_form (forms.ModelForm):
    class Meta:
        model = Reg
        widgets = {'pwd':forms.PasswordInput(),}
        fields = ['user','pwd','f_name','l_name','dob','mob_no']
class Log_form (forms.Form):
    user = forms.CharField(max_length=30)
    pwd = forms.CharField(widget=forms.PasswordInput())
