# Generated by Django 2.1.2 on 2019-02-12 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_mentor'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.URLField(default='default'),
            preserve_default=False,
        ),
    ]
