# Generated by Django 4.0 on 2022-01-23 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('Api', '0007_comment_like_remove_book_is_avaible_delete_borrow_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booklist', to='Api.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='added_user', to='auth.user')),
            ],
        ),
    ]