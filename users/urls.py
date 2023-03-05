from django.urls import path, include
from django.urls.resolvers import URLPattern
from users import views as view_reg
urlpatterns = [
    path('',view_reg.register,name='register'),
    
]
