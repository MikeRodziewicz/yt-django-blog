# Generated by Django 3.1.7 on 2021-03-19 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_auto_20210319_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click to read more', max_length=256),
        ),
    ]
