from django.shortcuts import render
from django.http import HttpResponse
from . models import Reg
from  .forms import Reg_form
from .forms import Log_form
# Create your views here.
def home (request):
    return render(request,"home.html")
def reg (request):
    if request.method=='POST':
        form1 = Reg_form(request.POST)
        if form1.is_valid():
            form1.save(commit=True)
            return HttpResponse("Registerd Successfully")
        else:
            print(form1.errors)
            return HttpResponse("Error Occured")
    else:
        form1=Reg_form()
        return render(request,"reg.html",{'form1':form1})
def log (request):
    if request.method=='POST':
        form2 = Log_form(request.POST)
        if form2.is_valid():
            un = form2.cleaned_data['user']
            pw = form2.cleaned_data['pwd']
            dbuser = Reg.objects.filter(user=un,pwd=pw)
            if not dbuser:
                return HttpResponse("Login Failed")
            else:
                return HttpResponse("login success")

    else:
        form2= Log_form()
        return render(request,"log.html",{'form2':form2})
