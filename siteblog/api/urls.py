from django.urls import path
from api.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('posts/', PostList.as_view(),),
    path('posts/<str:slug>/', PostDetail.as_view(),name="posts_view"),

]
urlpatterns = format_suffix_patterns(urlpatterns)     # for api/posts/?format= (api/json)