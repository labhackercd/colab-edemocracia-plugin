from django.conf.urls import patterns, url, include
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from colab_edemocracia.forms import accounts

from . import views

urlpatterns = patterns(
    '',
    url(r'^home/?$', views.login,
        {'template_name': 'home.html', 'redirect_field_name': 'previous_path'},
        name="home"),
    url(r'^signup/?$', views.SignUpView.as_view(), name="signup"),
    url(r'^profile/?$', login_required(views.ProfileView.as_view()),
        name="profile"),
    url(r'^profile/update_prefered_theme/$',
        login_required(views.UpdateUserPreferedTheme.as_view()),
        name="update_prefered_theme"),
    url(r'^profile/set_all_themes/$',
        login_required(views.SetAllThemes.as_view()),
        name="set_all_themes"),
    url(r'^search/', include('haystack.urls')),
    url(r'^password_change/$', 'colab_edemocracia.views.password_change',
        name='password_change'),
    url(r'^account/password-reset/?$', auth_views.password_reset,
        {'template_name': 'registration/password_reset_form_custom.html',
         'password_reset_form': accounts.PasswordResetForm},
        name="password_reset"),
    url(r'^password_change/done/$', auth_views.password_change_done,
        name='password_change_done'),
    url(r'^widget/login/$', views.WidgetLoginView.as_view(),
        name='widget_login'),
    url(r'^widget/signup/$', views.WidgetSignUpView.as_view(),
        name='widget_signup'),
    url(r'^widget/redirect/?$',
        TemplateView.as_view(template_name='widget/redirect.html'),
        name='redirect_widget'),
)
