from django.contrib import admin

# Register your models here.
from .models import *


class CityAdmin(admin.ModelAdmin):
    list_display = ('name','slug')

class OccupationAdmin(admin.ModelAdmin):
    list_display = ('name','slug')


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'company', 'city', 'occupation', 'timestamp')
    list_filter = ('city', 'timestamp', 'occupation')
    list_display_links = ('title',)
    search_fields = ('city', 'occupation')




admin.site.register(City, CityAdmin)
admin.site.register(Occupation, OccupationAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(Errors)
