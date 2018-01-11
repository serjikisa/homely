# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-10 22:13
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('baths', models.IntegerField(default=0)),
                ('rooms', models.IntegerField(default=0)),
                ('furnished', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Properties',
                'verbose_name': 'Property',
            },
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentals.Property')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cell_phone', models.CharField(blank=True, max_length=10, null=True, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_contact_no', message='contact_no must be Numeric', regex='^818[0-9]*$')], verbose_name='Cellphone')),
            ],
            options={
                'verbose_name_plural': 'users',
                'abstract': False,
                'verbose_name': 'user',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Homeowner',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rentals.UserProfile')),
            ],
            options={
                'verbose_name_plural': 'Homeowners',
                'verbose_name': 'Homeowner',
            },
            bases=('rentals.userprofile',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Renter',
            fields=[
                ('userprofile_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rentals.UserProfile')),
            ],
            options={
                'verbose_name_plural': 'Renters',
                'verbose_name': 'Renter',
            },
            bases=('rentals.userprofile',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='reserve',
            name='renter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentals.Renter'),
        ),
        migrations.AddField(
            model_name='property',
            name='homeowner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentals.Homeowner'),
        ),
    ]
