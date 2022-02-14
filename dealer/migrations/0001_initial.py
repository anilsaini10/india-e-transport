# Generated by Django 4.0.2 on 2022-02-13 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dealers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('contact', models.IntegerField(blank=True)),
                ('nature_of_material', models.CharField(blank=True, max_length=50)),
                ('weight_of_material', models.IntegerField(blank=True)),
                ('quantity', models.IntegerField(blank=True, default=1)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('state', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
