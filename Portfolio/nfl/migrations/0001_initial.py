# Generated by Django 2.1.2 on 2019-01-31 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(default=0)),
                ('hight', models.IntegerField(default=0)),
                ('weight', models.IntegerField(default=0)),
                ('position', models.CharField(max_length=100)),
                ('team', models.CharField(max_length=100)),
                ('passing_yards', models.IntegerField(default=0)),
                ('passing_touchdowns', models.IntegerField(default=0)),
                ('rushing_yards', models.IntegerField(default=0)),
                ('rushing_touchdowns', models.IntegerField(default=0)),
            ],
        ),
    ]
