# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _


User = get_user_model()


class SignUpForm(forms.ModelForm):

    error_messages = {
        'duplicate_email': _(u"Email já cadastrado."),
        'duplicate_username': _(u"Nome de usuário já cadastrado."),
    }

    required = ('username', 'email', 'password')

    class Meta:
        fields = ('username', 'email', 'password')
        model = User

    def clean_username(self):
        username = self.cleaned_data.get('username').strip().lower()
        if not username:
            raise forms.ValidationError(_('This field cannot be blank.'))

        if User.objects.filter(username=username).exists():
            msg = self.error_messages.get('duplicate_username')
            raise forms.ValidationError(mark_safe(msg))

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')

        user_qs = User.objects.filter(email=email).exclude(username=username)

        if email and user_qs.exists():
            msg = self.error_messages.get('duplicate_email')
            raise forms.ValidationError(mark_safe(msg))

        return email
