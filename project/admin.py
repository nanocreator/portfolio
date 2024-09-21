from django.contrib import admin
from .models import Category, Projet


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('titre', 'link', 'date_created', 'date_updated', 'status', 'category')
    list_filter = ('status', 'category')
    search_fields = ('titre', 'description')
    prepopulated_fields = {'slug': ('titre',)}
    date_hierarchy = 'date_created'
    ordering = ('-date_created',)
