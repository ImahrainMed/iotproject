# Generated by Django 3.2.8 on 2021-12-05 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fridge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255, null=True)),
                ('location', models.CharField(max_length=255, null=True)),
                ('creation', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dht11',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp', models.FloatField(null=True)),
                ('hum', models.FloatField(null=True)),
                ('dt', models.DateTimeField(auto_now_add=True, null=True)),
                ('min_critical_tem', models.FloatField(null=True)),
                ('max_severe_tem', models.FloatField(null=True)),
                ('max_critical_tem', models.FloatField(null=True)),
                ('min_severe_tem', models.FloatField(null=True)),
                ('fridge', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dht11s', to='myapp.fridge', verbose_name='Agence')),
            ],
        ),
    ]