# Generated by Django 3.2.15 on 2022-11-20 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_book_pdf_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='mp3_file',
            field=models.FileField(null=True, upload_to='mp3_files/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pdf_file',
            field=models.FileField(null=True, upload_to='pdf_files/'),
        ),
    ]
