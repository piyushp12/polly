# Generated by Django 4.1 on 2022-08-26 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pollyhouse_app', '0005_remove_signup_district_remove_signup_pin_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='avatar',
        ),
    ]
