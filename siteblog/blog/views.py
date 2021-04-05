from django.contrib.auth import login, logout
from django.shortcuts import render, redirect, get_object_or_404
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
        context["title"] = "All posts by tag: " + str(Tag.objects.get(slug=self.kwargs["slug"]))
        return context


def single_post(request, slug):
    template_name = 'blog/single.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    post.views = F("views") + 1
    post.save()
    post.refresh_from_db()
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentsForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentsForm()

    context = {'post': post,
               'comments': comments,
               'new_comment': new_comment,
               'form': comment_form}

    return render(request, template_name, context)


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
    template_name = "blog/single.html"

    # def get_initial(self):
    #     initial = super(AddComments, self).get_initial()
    #     initial.update({"username": self.request.user.username})
    #     return initial

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     prev_page = self.request.META.get('HTTP_REFERER')
    #
    #     context["s"] =
    #     return context

    def form_valid(self, form):
        redirect = self.request.META.get('HTTP_REFERER')  # to previous page
        if redirect:
            redirect += "#comment"  # to anchor
            self.success_url = redirect
        return super(AddComments, self).form_valid(form)

    # def form_invalid(self, form):                           not working -------fix later
    #     print("form invalid")
    #     print(super(AddComments, self).form_invalid(form))
    #     redirect = self.request.META.get('HTTP_REFERER')  # to previous page
    #     print(form)
    #
    #     if redirect:
    #         redirect += "#comment"  # to anchor
    #         self.unsuccess_url = redirect
    #         print(redirect)
    #
    #     return super(AddComments, self).form_invalid(form)
