# Generated by Django 4.2 on 2023-04-29 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='namme',
            new_name='name',
        ),
    ]
