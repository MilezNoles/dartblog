from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView

from blog.forms import *
from blog.models import *
from django.db.models import F



def register(request):
    if request.method == "POST":
        form = UserRegister(request.POST)  # связь формы с данными
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")


    else:
        form = UserRegister()

    context = {
        "form": form,
    }
    return render(request, "blog/register.html", context)


def user_login(request):
    if request.method == "POST":
        form = UserLogin(data=request.POST)  # для логина обязательна data=
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect("home")



    else:
        form = UserLogin()

    context = {
        "form": form,
    }
    return render(request, "blog/login.html", context)


def user_logout(request):
    logout(request)
    return redirect("login")


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




class PostsByCategory(ListView):
    template_name = "blog/category.html"
    context_object_name = "posts"
    paginate_by = 4
    allow_empty = False


    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs["slug"])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = Category.objects.get(slug=self.kwargs["slug"])
        return context


class PostsByTag(ListView):
    pass

class GetPost(DetailView):
    model = Post
    template_name = "blog/single.html"
    context_object_name = "post"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F("views") + 1
        self.object.save()
        self.object.refresh_from_db()
        return context




