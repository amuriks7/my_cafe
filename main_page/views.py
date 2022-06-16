from django.shortcuts import render, redirect
from .models import Category, Dish
from .forms import UserReservationForm


def main_page(request):

    categories = Category.objects.filter(is_visible=True).order_by('position')
    dishes = Dish.objects.filter(is_visible=True).order_by('position')

    return render(request, 'main.html', context={'categories': categories, 'dishes': dishes})
