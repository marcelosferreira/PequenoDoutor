# Generated by Django 3.1.7 on 2022-05-13 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0026_auto_20220513_0009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='alunoChat',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='mensagemChat',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='turmaChat',
        ),
    ]
