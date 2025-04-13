from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class GalleryInline(admin.TabularInline):
    fk_name = 'project'
    model = Gallery
    extra = 1


@admin.register(Project)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'client', 'title', 'project_url', 'get_photo', 'created_at')
    list_display_links = ('name',)
    prepopulated_fields = {"slug": ("name",)}
    inlines = [GalleryInline]

    def get_photo(self, obj):
        if obj.images:
            try:
                return mark_safe(f'<img src="{obj.images.all()[0].image.url}" width="75">')
            except:
                return 'NO PHOTO'
        else:
            return 'NO PHOTO'

