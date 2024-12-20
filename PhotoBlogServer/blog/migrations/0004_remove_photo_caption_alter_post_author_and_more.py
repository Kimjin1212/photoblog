# Generated by Django 5.1.1 on 2024-11-04 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_tags_alter_post_text_alter_post_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='caption',
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
