from django.contrib import admin
from .models import Category, Post


#admin.site.register([Category, Post])


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug') # отображение полей
    search_fields = ('name',) # поиск по 'name'
    prepopulated_fields = {'slug': ('name',)} # для авто заполнения поля слаг = по полю 'name'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    search_fields = ('title', 'body')
    list_filter = ('status', 'created', 'author')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-status', '-publish')
    raw_id_fields = ('author',)
