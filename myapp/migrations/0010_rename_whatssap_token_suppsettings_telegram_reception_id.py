# Generated by Django 3.2.8 on 2021-12-19 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_asset_min_severe_telemetry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='suppsettings',
            old_name='whatssap_token',
            new_name='telegram_reception_id',
        ),
    ]