# Generated by Django 3.1.4 on 2022-03-17 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20220317_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api_key',
            name='last_called',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
