# -*- coding: utf-8 -*-
from django import forms
from django.core.mail import send_mail


class FormContact(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    message = forms.Field(widget=forms.Textarea, required=True)
    site = forms.URLField(required=False)

    def send(self):
        title = 'e-Democracia - Contato'
        target = 'edemocracia@camara.leg.br'
        text = """
        Site de origem: %(site)s
        Nome: %(name)s
        E-mail: %(email)s
        Mensagem: %(message)s
        """ % self.cleaned_data

        send_mail(
            subject=title,
            message=text,
            from_email=target,
            recipient_list=[target],
        )
