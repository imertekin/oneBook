# Generated by Django 4.0 on 2021-12-15 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ISBN', models.CharField(max_length=13, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('Author', models.CharField(max_length=50)),
                ('Publisher', models.CharField(max_length=50)),
                ('Publication_date', models.DateTimeField()),
                ('Genres', models.CharField(max_length=50)),
                ('Print_length', models.PositiveSmallIntegerField()),
                ('is_avaible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='borrow_book', to='Api.books')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrow_user', to='auth.user')),
            ],
        ),
    ]