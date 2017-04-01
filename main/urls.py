from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^date/$', views.date_actuelle),   
    url('', views.home),    
]