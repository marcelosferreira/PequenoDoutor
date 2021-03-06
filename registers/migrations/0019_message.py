# Generated by Django 3.1.7 on 2021-06-13 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0018_remove_chat_datamensagemchat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('room', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('date_added',),
            },
        ),
    ]
