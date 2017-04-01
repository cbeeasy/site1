from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^date/$', views.date_actuelle), 
    url(r'^test/$', views.test),  
    url(r'', views.home),    
] 