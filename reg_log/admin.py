from django.contrib import admin
from . models import Reg
# Register your models here.
class Reg_admin(admin.ModelAdmin):
    list_display = ['user','f_name','l_name','dob','mob_no']
    list_filter = ['dob']
    class meta:
        models = Reg
admin.site.register(Reg,Reg_admin)