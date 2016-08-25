from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = patterns(
    '',
    url(r'^home/?$', views.login,
        {'template_name': 'home.html', 'redirect_field_name': 'previous_path'},
        name="home"),
    url(r'^signup/?$', views.SignUpView.as_view(), name="signup"),
    url(r'^profile/?$', login_required(views.ProfileView.as_view()),
        name="profile"),
)
