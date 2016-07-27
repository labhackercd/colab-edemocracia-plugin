
from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = patterns(
    '',
    url(r'^home/?$', auth_views.login,
        {'template_name': 'home.html', 'extra_context': views.get_home_data(),
         'redirect_field_name': 'previous_path'},
        name="home"),
)
