# Generated by Django 4.2.16 on 2024-11-05 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_author_alter_post_tags_alter_post_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='tags',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
