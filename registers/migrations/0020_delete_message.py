# Generated by Django 3.1.7 on 2021-06-13 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0019_message'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
    ]