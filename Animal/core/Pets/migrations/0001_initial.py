# Generated by Django 5.1.2 on 2024-11-01 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('breed', models.CharField(max_length=255)),
                ('gender', models.IntegerField(default=1)),
                ('description', models.TextField()),
                ('posted_at', models.DateTimeField(auto_now_add=True)),
                ('pet_image', models.ImageField(blank=True, null=True, upload_to='category/')),
                ('category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PetCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_image', models.ImageField(blank=True, null=True, upload_to='category/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
