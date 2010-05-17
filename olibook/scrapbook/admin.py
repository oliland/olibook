from django.contrib import admin
from scrapbook.models import BlogEntry

class BlogEntryAdmin(admin.ModelAdmin):
    fields=('author', 'title', 'slug', 'body')
    list_display=('title', 'author', 'created')
    date_hierarchy='created'
    prepopulated_fields={'slug': ('title', )}

admin.site.register(BlogEntry, BlogEntryAdmin)
