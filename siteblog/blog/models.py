from django.db import models
'''
Category
-----------
title, slug

Tag
________
title, slug

Post
-------------
title, slug, author, context, created_at, photo, views, category, 
'''

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Категория",)
    slug = models.SlugField(max_length=255, verbose_name="Url", unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["title"]



class Tag(models.Model):
    title = models.CharField(max_length=50, verbose_name="Тэг",)
    slug = models.SlugField(max_length=50, verbose_name="Url", unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"
        ordering = ["title"]


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок",)
    slug = models.SlugField(max_length=255, verbose_name="Url", unique=True)
    author = models.CharField(max_length=100, verbose_name="Автор", )
    context = models.TextField(blank=True, verbose_name="Контекст", )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания", )
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True, verbose_name="Фото", )
    views = models.IntegerField(default=0, verbose_name="Количество просмотров", )
    category = models.ForeignKey(Category, on_delete=models.PROTECT,related_name="posts", verbose_name="Категория", )
    tags  = models.ManyToManyField(Tag, blank=True, related_name="posts", verbose_name="Тэг",)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-created_at"]