# Generated by Django 2.2.2 on 2019-06-27 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='created_at',
        ),
    ]
