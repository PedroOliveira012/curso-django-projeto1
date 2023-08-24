# from django.http import HttpResponse
from django.shortcuts import render

from .models import Recipe
from .utils.recipes.factory import make_recipe


# Create your views here.
def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
