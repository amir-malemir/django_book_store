# Generated by Django 5.0.4 on 2024-05-17 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_book_cover'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='book_cover',
            new_name='cover',
        ),
    ]
