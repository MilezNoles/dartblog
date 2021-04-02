from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.models import User

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
    template_name = "blog/category.html"
    context_object_name = "posts"
    paginate_by = 4
    allow_empty = False


    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs["slug"])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] ="All posts by tag: " + str(Tag.objects.get(slug=self.kwargs["slug"]))
        return context





class GetPost(DetailView):
    model = Post
    template_name = "blog/single.html"
    context_object_name = "post"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F("views") + 1
        self.object.save()
        self.object.refresh_from_db()
        context["comments"] = Comments.objects.all()
        return context


# class PersonalPage(DetailView):
#     model = Post
#     template_name = "blog/personal.html"
#     context_object_name = "post"
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         self.object.views = F("views") + 1
#         self.object.save()
#         self.object.refresh_from_db()
#         context["user"] = User.objects.get(pk=self.kwargs["pk"])
#         return context
#
#     def get_queryset(self):
#         user = User.objects.get(pk=self.kwargs["pk"])
#         print(user.username)
#         return Post.objects.filter(author=user.username, )


class Search(ListView):
    template_name = "blog/search.html"
    context_object_name = "posts"
    paginate_by = 4

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get("s"))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["s"] = f"s={self.request.GET.get('s')}&"
        return context


class AddComments(CreateView):
    form_class = CommentsForm
    template_name = "blog/index.html"



    def form_valid(self, form):
        redirect = self.request.META.get('HTTP_REFERER')   # to previous page
        if redirect:
            redirect += "#comment"      # to anchor
            self.success_url = redirect
            print(redirect)
        return super(AddComments, self).form_valid(form)


    # def get_initial(self):
    #     initial = super(AddComments, self).get_initial()
    #     initial.update({"nickname": self.request.user.username})
    #     return initial
