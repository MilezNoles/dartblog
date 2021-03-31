from django.db import models, transaction
from django.urls import reverse_lazy

'''
Category
-----------
title, slug

Tag
________
title, slug

Post
-------------
title, slug, author, content, created_at, photo, views, category, 
'''

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Category",)
    slug = models.SlugField(max_length=255, verbose_name="Url", unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # для ссылок
        return reverse_lazy("category", kwargs={"slug": self.slug, })

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["title"]



class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name="Tag",)
    slug = models.SlugField(max_length=50, verbose_name="Url", unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # для ссылок
        return reverse_lazy("tag", kwargs={"slug": self.slug, })

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
        ordering = ["title"]


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title",)
    slug = models.SlugField(max_length=255, verbose_name="Url", unique=True)
    author = models.CharField(max_length=100, verbose_name="Author", )
    content = models.TextField(verbose_name="Content",blank=True,)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creation date", )
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Photo", )
    views = models.IntegerField(default=0, verbose_name="Views", )
    category = models.ForeignKey(Category, on_delete=models.PROTECT,related_name="posts", verbose_name="Category", )
    tags  = models.ManyToManyField(Tag, blank=True, related_name="posts", verbose_name="Tag",)
    is_main = models.BooleanField(default=False, verbose_name="On main?")

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # для ссылок
        return reverse_lazy("post", kwargs={"slug": self.slug, })

    @transaction.atomic  #для того чтобы в is_main был только один True
    def save(self, *args, **kwargs):
        if self.is_main:
            Post.objects.filter(
                is_main=True).update(is_main=False)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-created_at"]


class Comments(models.Model):
    username = models.CharField(max_length=50, verbose_name="Username", )  # обязательный атрибут - длина
    comment = models.TextField(verbose_name="Comment")  # по умолчанию пустой
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")  # про создании новости
    # поставится не изменяемая дата и время,которые будут взяты в момент создания
    # фото будут сохраняться в папке фото/год.месяц.день

    # def get_absolute_url(self):  # для ссылок
    #     return reverse_lazy("comments")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Comment"  # имя в админке ед число
        verbose_name_plural = "Comments"
        ordering = ["created_at"]