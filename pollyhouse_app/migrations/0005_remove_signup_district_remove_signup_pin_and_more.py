# Generated by Django 4.1 on 2022-08-26 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollyhouse_app', '0004_alter_signup_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='district',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='pin',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='state',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='village',
        ),
    ]
