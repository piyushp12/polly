# Generated by Django 4.1 on 2022-08-27 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pollyhouse_app', '0008_remove_signup_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='district_name', to='pollyhouse_app.district'),
        ),
        migrations.AddField(
            model_name='signup',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='state_name', to='pollyhouse_app.state'),
        ),
        migrations.AddField(
            model_name='signup',
            name='village',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='village_name', to='pollyhouse_app.village'),
        ),
    ]