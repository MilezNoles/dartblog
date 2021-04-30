from django.urls import path
from jobscrapper.views import *

urlpatterns = [
    path('', vacancies_view, name="vacancy"),

]