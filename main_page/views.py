from django.shortcuts import render
from .models import Category, Dish


def main_page(request):
    categories = Category.objects.filter(is_visible=True).order_by('position')
    dishes = Dish.objects.filter(is_visible=True).order_by('position')

    return render(request, 'main.html', context={'categories': categories, 'dishes': dishes})


def render_typography_page(request):
    return render(request, 'typography.html', context={})


def about_new(request):
    return render(request, 'about.html', context={})