# Generated by Django 3.2.22 on 2023-11-06 21:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dogblog', '0002_alter_dogphoto_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='likephoto',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='blog_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
