from django.contrib import admin
from .models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'posted']
    list_filter = ['posted']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    class Meta:
        model = Blog

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
