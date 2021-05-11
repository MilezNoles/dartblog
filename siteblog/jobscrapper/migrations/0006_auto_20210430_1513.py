# Generated by Django 3.1.7 on 2021-04-30 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobscrapper', '0005_auto_20210430_1347'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='occupation',
            options={'ordering': ['name'], 'verbose_name': 'Специальность', 'verbose_name_plural': 'Специальности'},
        ),
        migrations.AlterField(
            model_name='occupation',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Специальность'),
        ),
    ]
