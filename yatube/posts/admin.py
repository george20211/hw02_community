from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Post

User = get_user_model()


class Admin(admin.ModelAdmin):
    list_display = ('text', 'pub_date', 'author', 'group',)
    list_filter = ('text', 'pub_date')
    search_fields = ("text",)
    empty_value_display = "-пусто-"


admin.site.register(Post, Admin)
