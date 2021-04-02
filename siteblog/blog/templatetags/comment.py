from django import template
from django.shortcuts import redirect

from blog.models import Post, Tag
from django.db.models import *
from blog.forms import *

register = template.Library()



@register.inclusion_tag('blog/add_comments.html', takes_context=True)
def add_comments(context):
    request = context['request']
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("post")

    else:
        form = CommentsForm()
    context = {
        "form": form,
    }
    return context

