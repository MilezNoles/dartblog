# Generated by Django 3.1.7 on 2021-04-05 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_comments_avatar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['created_at']},
        ),
        migrations.AddField(
            model_name='comments',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='username',
            field=models.CharField(max_length=80, verbose_name='Username'),
        ),
    ]
