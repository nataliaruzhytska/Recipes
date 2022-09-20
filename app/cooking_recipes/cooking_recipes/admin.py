from django.contrib import admin
from .models import Recipes, Category


@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category')
    search_fields = ('title', 'category')
    list_filter = ('title', 'category')


@admin.register(Category)
class RecipesAdmin(admin.ModelAdmin):
    list_display = 'name'
    search_fields = 'name'
    list_filter = 'name'
