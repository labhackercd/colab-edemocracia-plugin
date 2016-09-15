# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _
from colab_edemocracia.models import UserProfile


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


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].initial = kwargs['instance'].user.first_name
        self.fields['last_name'].initial = kwargs['instance'].user.last_name
        self.fields['gender'].initial = kwargs['instance'].gender
        self.fields['uf'].initial = kwargs['instance'].uf
        self.fields['birthdate'].initial = kwargs['instance'].birthdate

    class Meta:
        fields = ('gender', 'uf', 'birthdate', 'first_name', 'last_name')
        model = UserProfile

    def save(self, commit=True):
        instance = super(UserProfileForm, self).save(commit=False)
        instance.save()
        instance.user.first_name = self.cleaned_data['first_name']
        instance.user.last_name = self.cleaned_data['last_name']
        if commit:
            instance.user.save()
        return instance
