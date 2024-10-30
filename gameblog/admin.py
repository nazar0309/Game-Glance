from django.contrib import admin
from .models import Game
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Game)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'created_on', 'genre')
    search_fields = ['title', 'description', 'genre', 'company']
    list_filter = ('updated_on', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

