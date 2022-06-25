from django.urls import path

from django.conf.urls.static import settings
from django.conf.urls.static import static

from .views import main_page, render_typography_page, about_new

app_name = 'main_page'

urlpatterns = [
    path('', main_page, name='main_page_view'),
    path('typography/', render_typography_page, name='typography_view'),
    path('about/', about_new, name='about_view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)