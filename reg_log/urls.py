from django.conf.urls import url
from . import views
app_name = "reg_log"
urlpatterns =[
    url(r'^$',views.home),
    url(r'^reg$',views.reg),
    url(r'^log$',views.log),
]