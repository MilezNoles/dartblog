from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import *

class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = PostAdminForm
    save_as = True
    save_on_top = True  # кнопки сохранить будут и вверху
    list_display = (
        "id", "title","slug", "category", "created_at", "get_photo","is_main")  # столбцы в админке
    list_display_links = ("id", "title")  # что будет ссылкой на редактирование в админке
    search_fields = ("title",)  # search in admin
    list_editable = ("category","is_main",)
    list_filter = ("category",)

    readonly_fields = ("views", "created_at", "get_photo", )  # поля которые будут только для чтения
    fields =("title","slug", "category","tags","author", "content", "photo", "get_photo","views", "created_at","is_main")


    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width='50'>")  # убирает экранирование
        else:
            return " - "

    get_photo.short_description = "Preview"  # Меняем вывод Getphoto в столбце админки на Preview


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        "id", "title", "slug",)  # столбцы в админке
    list_display_links = ("id", "title")  # что будет ссылкой на редактирование в админке

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        "id", "title", "slug",)  # столбцы в админке
    list_display_links = ("id", "title")  # что будет ссылкой на редактирование в админке

class CommentsAdmin(admin.ModelAdmin):
    list_display = (
        "id", "username", "created_at")  # столбцы в админке
    list_display_links = ("id", "username")  # что будет ссылкой на редактирование в админке



admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comments, CommentsAdmin)


