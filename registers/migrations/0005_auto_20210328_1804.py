# Generated by Django 3.1.7 on 2021-03-28 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0004_auto_20210328_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='professorAluno',
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCurso', models.CharField(max_length=255)),
                ('variosAtributosCurso', models.CharField(max_length=255)),
                ('quantidadeAulasCurso', models.CharField(max_length=255)),
                ('professorCurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registers.professor')),
            ],
        ),
        migrations.AddField(
            model_name='aluno',
            name='cursoAluno',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='registers.curso'),
            preserve_default=False,
        ),
    ]