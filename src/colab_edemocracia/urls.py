from django.conf.urls import patterns, url, include
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
    url(r'^profile/update_prefered_theme/$',
        login_required(views.UpdateUserPreferedTheme.as_view()),
        name="update_prefered_theme"),
    url(r'^profile/set_all_themes/$',
        login_required(views.SetAllThemes.as_view()),
        name="set_all_themes"),
    url(r'^search/', include('haystack.urls')),
    url(r'^password_change/$', 'colab_edemocracia.views.password_change',
        name='password_change'),
    url(r'^password_change/done/$', 'django.contrib.auth.views.password_change_done',
        name='password_change_done'),
    url(r'^widget/login/$', views.WidgetLoginView.as_view(),
        name='widget_login'),
    url(r'^widget/signup/$', views.WidgetSignUpView.as_view(),
        name='widget_signup'),
    url(r'^widget/logout/$', views.WidgetLogoutView.as_view(),
        name='widget_logout'),
)
