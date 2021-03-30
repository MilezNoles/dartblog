from django.urls import path
from blog.views import *

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('category/<str:slug>/', PostsByCategory.as_view(), name="category"),
    path('post/<str:slug>/',get_post, name="post"),
]