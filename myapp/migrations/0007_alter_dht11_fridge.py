# Generated by Django 3.2.8 on 2021-12-13 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20211213_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dht11',
            name='fridge',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dht11s', to='myapp.fridge', verbose_name='Fridge'),
        ),
    ]