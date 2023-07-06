from django.urls import path
from . import views
urlpatterns = [
    path('registerhome/',views.registerhome,name='registerhome'),
    path('login/',views.login,name='login')
    ]