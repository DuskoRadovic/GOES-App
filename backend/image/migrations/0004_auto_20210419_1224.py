# Generated by Django 3.1.7 on 2021-04-19 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0003_auto_20210419_0016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['id']},
        ),
    ]
