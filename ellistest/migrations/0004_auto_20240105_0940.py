# Generated by Django 3.0 on 2024-01-05 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ellistest', '0003_auto_20240105_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
