from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('yoga_centres/',views.yoga_centres,name = 'yoga_centres'),]

