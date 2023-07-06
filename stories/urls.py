from django.urls import path
from .views import PostCreateView
from . import views
urlpatterns = [
    path('showstories/',views.showstories,name = 'showstories'),
    path('post/new/',PostCreateView.as_view(),name = 'post_create'),
    ]