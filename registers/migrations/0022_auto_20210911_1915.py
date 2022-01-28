# Generated by Django 3.1.7 on 2021-09-11 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0021_message_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='turmasAluno',
        ),
        migrations.AddField(
            model_name='aluno',
            name='turmaAluno',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='registers.turma'),
        ),
    ]