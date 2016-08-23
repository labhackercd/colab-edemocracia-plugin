from django.views.generic import View
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from .forms.accounts import SignUpForm
from colab.accounts.models import EmailAddressValidation, EmailAddress


User = get_user_model()


class SignUpView(View):
    http_method_names = [u'post']

    def post(self, request):
        if request.user.is_authenticated():
            return reverse('colab_edemocracia:home')

        user_form = SignUpForm(request.POST)

        if not user_form.is_valid():
            return render(request, 'home.html',
                          {'user_form': user_form, })

        user = user_form.save(commit=False)
        user.needs_update = False

        user.is_active = False
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
            email_addr.real_name = user.get_full_name()

        email_addr.user = user
        email_addr.save()

        return redirect(reverse('colab_edemocracia:home'))
