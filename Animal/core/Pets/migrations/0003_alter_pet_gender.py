# Generated by Django 5.1.2 on 2024-11-05 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pets', '0002_remove_petcategory_category_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='gender',
            field=models.CharField(max_length=10),
        ),
    ]
