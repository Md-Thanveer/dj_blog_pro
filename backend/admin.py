from django.contrib import admin

# Register your models here.
from backend.models import Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = ('name',)