# Generated by Django 3.1.7 on 2021-04-30 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobscrapper', '0004_auto_20210429_2115'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Language',
            new_name='Occupation',
        ),
        migrations.RenameField(
            model_name='vacancy',
            old_name='lang',
            new_name='occupation',
        ),
    ]