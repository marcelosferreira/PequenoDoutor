# Generated by Django 3.1.7 on 2021-03-28 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0008_aluno_cursoaluno'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='categoriaCurso',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
