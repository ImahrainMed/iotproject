# Generated by Django 3.2.8 on 2021-12-12 17:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0004_alter_suppsettings_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='fridge',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fridges', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
