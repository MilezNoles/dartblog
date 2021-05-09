# Generated by Django 3.1.7 on 2021-04-06 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210405_2349'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['created_at'], 'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterField(
            model_name='comments',
            name='username',
            field=models.CharField(blank=True, max_length=80, verbose_name='Username'),
        ),
    ]