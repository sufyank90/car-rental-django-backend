# Generated by Django 5.0.6 on 2024-05-31 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('image_url', models.URLField(blank=True)),
                ('fuel', models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Electric', 'Electric'), ('Hybrid', 'Hybrid')], max_length=10)),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Sold', 'Sold'), ('Reserved', 'Reserved')], max_length=10)),
                ('brand', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]