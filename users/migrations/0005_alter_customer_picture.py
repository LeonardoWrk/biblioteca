# Generated by Django 3.2.15 on 2022-11-22 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20221108_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='picture',
            field=models.ImageField(blank=True, default='default_pic.ico', null=True, upload_to='profiles/'),
        ),
    ]