from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView

from blog.models import *


class Home(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by = 4


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context["title"] = "Blog Design"
        context["main"] = Post.objects.get(is_main=True)

        return context





def get_category(request, slug):
    return render(request, 'blog/category.html')

def get_post(request, slug):
    return render(request, 'blog/category.html')


