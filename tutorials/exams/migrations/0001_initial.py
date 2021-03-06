# Generated by Django 2.2.2 on 2019-06-27 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=500)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('grade', models.CharField(blank='True', choices=[('pass', 'pass'), ('fail', 'fail')], max_length=5, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('questions', models.ManyToManyField(related_name='exams', to='questions.Question')),
            ],
        ),
    ]
