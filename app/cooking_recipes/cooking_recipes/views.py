from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic import ListView, DetailView

from .models import Recipes, Category


def health_check(request):
    return HttpResponse('OK')


def index(request):
    return HttpResponse(render_to_string('index.html', {'title': 'Cooking recipes'}))


class RecipesListView(ListView):
    model = Recipes
    queryset = Recipes.objects.all()
    template_name = 'recipes_list.html'
    paginate_by = 30

    def get_all_recipes(self):
        return self.queryset.all()


class CategoriesListView(ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = 'categories_list.html'
    paginate_by = 30

    def get_all_categories(self):
        return self.queryset.all()


class RecipeDetailView(DetailView):
    model = Recipes()
    queryset = Recipes.objects.all()
    template_name = 'recipe_detail.html'

    def get_recipe(self):
        return self.queryset.filter(recipes_id=self.kwargs.get('recipes_id'))


class CategoryDetailView(DetailView):
    model = Category()
    queryset = Category.objects.all()
    template_name = 'category_detail.html'

    def get_category(self):
        return self.queryset.filter(category_id=self.kwargs.get('category_id'))
