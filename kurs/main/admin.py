from django.contrib import admin
from .models import *
from .models import News

admin.site.register(Cheatsheet)

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    search_fields = ('title', 'content')

admin.site.register(News, NewsAdmin)


