# Generated by Django 4.0 on 2022-01-01 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0004_book_image_borrow_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/%Y/%m/%d'),
        ),
    ]