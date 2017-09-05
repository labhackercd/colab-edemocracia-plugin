# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from colab_edemocracia.views import generate_username
from django.db import transaction
import csv

User = get_user_model()


class Command(BaseCommand):
    args = '<filename>'

    @transaction.atomic
    def handle(self, *args, **kwargs):
        if len(args) == 0:
            raise CommandError('You must set a filename.')

        filename = args[0]
        with open(filename) as f:
            reader = csv.reader(f, delimiter=";")
            for row in reader:
                email = row[0]
                try:
                    user = User.objects.get(email=email)
                except User.DoesNotExist:
                    user = User()
                    user.email = email

                name = '{} {} {}'.format(row[1], row[2], row[3])
                user.first_name = ' '.join(name.split()).title()
                user.last_name = ''
                user.username = generate_username(user.email)
                user.save()
                user.profile.uf = row[5]
                user.profile.save()
                print('Updating {} data'.format(user.first_name))
