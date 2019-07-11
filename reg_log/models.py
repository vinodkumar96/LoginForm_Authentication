from django.db import models

# Create your models here.
class Reg (models.Model):
    user = models.CharField(primary_key=True,max_length=20)
    pwd = models.CharField(max_length=20)
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    dob = models.DateField()
    mob_no = models.IntegerField()
