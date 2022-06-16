from django.urls import path
from .views import main_page, render_typography_page

app_name = 'main_page'

urlpatterns = [
    path('', main_page, name='main_page_view'),
    path('typography/', render_typography_page, name='typography_view'),
]