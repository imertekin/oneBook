# Generated by Django 4.0 on 2022-01-10 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0005_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d'),
        ),
    ]
