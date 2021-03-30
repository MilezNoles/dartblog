from django.urls import path
from blog.views import *

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('category/<str:slug>/',get_category, name="category"),
    path('post/<str:slug>/',get_post, name="post"),
]