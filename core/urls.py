from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^gui_home$',
        views.get_home, name='gui_home'),
]
