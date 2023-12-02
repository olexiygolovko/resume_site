from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('languages/', language, name='language'),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('img/favicon.ico')))
]