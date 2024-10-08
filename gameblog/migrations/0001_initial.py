# Generated by Django 4.2.15 on 2024-09-26 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=2000, unique=True)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('company', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=50)),
                ('platform', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
