# Generated by Django 4.0.2 on 2022-02-14 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dealer', '0002_drivers_dealers_email_dealers_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dealers_Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('contact', models.IntegerField(blank=True)),
                ('nature_of_material', models.CharField(blank=True, max_length=50)),
                ('weight_of_material', models.IntegerField(blank=True)),
                ('quantity', models.IntegerField(blank=True, default=1)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('state', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Drivers_Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50)),
                ('name', models.CharField(blank=True, max_length=50)),
                ('email', models.CharField(blank=True, max_length=50)),
                ('age', models.IntegerField(blank=True)),
                ('truck_number', models.CharField(blank=True, max_length=16)),
                ('contact', models.IntegerField(blank=True)),
                ('truck_capacity', models.IntegerField(blank=True)),
                ('transporter_name', models.CharField(blank=True, max_length=50)),
                ('driving_experience', models.IntegerField(blank=True)),
                ('city1', models.CharField(blank=True, max_length=20)),
                ('state1', models.CharField(blank=True, max_length=20)),
                ('city2', models.CharField(blank=True, max_length=20)),
                ('state2', models.CharField(blank=True, max_length=20)),
                ('city3', models.CharField(blank=True, max_length=20)),
                ('state3', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Dealers',
        ),
        migrations.DeleteModel(
            name='Drivers',
        ),
    ]