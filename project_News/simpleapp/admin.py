from django.contrib import admin
from .models import News, News_Category


admin.site.register(News)
admin.site.register(News_Category)