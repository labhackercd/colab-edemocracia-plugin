# -*- coding: utf-8 -*-
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render_to_response, resolve_url
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.utils.http import is_safe_url
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth import (REDIRECT_FIELD_NAME, login as auth_login)
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.response import TemplateResponse

from .forms.accounts import SignUpForm
from colab.accounts.models import EmailAddressValidation, EmailAddress
from colab_wikilegis.models import WikilegisBill
from colab_discourse.models import DiscourseTopic, DiscourseCategory


User = get_user_model()


@sensitive_post_parameters()
@csrf_protect
@never_cache
def login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          current_app=None, extra_context=None):
    """
    Displays the login form and handles the login action.
    """
    redirect_to = request.POST.get(redirect_field_name,
                                   request.GET.get(redirect_field_name, ''))

    if request.method == "POST":
        form = authentication_form(request, data=request.POST)
        if form.is_valid():

            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

            # Okay, security check complete. Log the user in.
            auth_login(request, form.get_user())

            return HttpResponseRedirect(redirect_to)
        else:
            messages.add_message(request, messages.ERROR,
                                 u"Usuário ou senhas incorretos.")
    else:
        form = authentication_form(request)

    current_site = get_current_site(request)

    wikilegis_data = WikilegisBill.objects.filter(status='published')
    wikilegis_data = wikilegis_data.order_by('-modified')
    discourse_data = DiscourseTopic.objects.all().order_by('-last_posted_at')

    context = {
        'form': form,
        redirect_field_name: redirect_to,
        'site': current_site,
        'site_name': current_site.name,
        'wikilegis_data': wikilegis_data,
        'discourse_data': discourse_data,
    }

    return TemplateResponse(request, template_name, context,
                            current_app=current_app)


class SignUpView(View):
    http_method_names = [u'post']

    def post(self, request):
        if request.user.is_authenticated():
            return reverse('colab_edemocracia:home')

        user_form = SignUpForm(request.POST)

        if not user_form.is_valid():
            for error in user_form.errors.values():
                messages.add_message(request, messages.ERROR, error[0])
            return redirect(reverse('colab_edemocracia:home'))

        user = user_form.save(commit=False)
        user.needs_update = False

        user.is_active = False
        user.set_password(user_form.cleaned_data['password'])
        user.save()

        email = EmailAddressValidation.create(user.email, user)

        location = reverse('email_view',
                           kwargs={'key': email.validation_key})
        verification_url = request.build_absolute_uri(location)
        EmailAddressValidation.verify_email(email, verification_url)

        # Check if the user's email have been used previously in the mainling
        # lists to link the user to old messages
        email_addr, created = EmailAddress.objects.get_or_create(
            address=user.email)
        if created:
            messages.add_message(
                request, messages.SUCCESS,
                u"Usuário criado com sucesso! Por favor, verifique seu email"
                " para concluir seu cadastro."
            )
            email_addr.real_name = user.get_full_name()

        email_addr.user = user
        email_addr.save()

        return redirect(reverse('colab_edemocracia:home'))


class ProfileView(View):

    def get(self, request):
        categories = DiscourseCategory.objects.all()
        return render_to_response('profile.html', {'categories': categories})
