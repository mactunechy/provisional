# Generated by Django 2.2.2 on 2019-06-28 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190628_1124'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='subsription',
            new_name='subscription',
        ),
    ]
