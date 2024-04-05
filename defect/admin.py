from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Defect, Update


@admin.register(Defect)
class DefectAdmin(SummernoteModelAdmin):
    list_display = ('title', 'category', 'author', 'reported_on', 'status')
    search_fields = ['title']
    list_filter = ('status', 'category', 'reported_on')
    summernote_fields = ('body',)


# Register your models here.
admin.site.register(Category)
admin.site.register(Update)
