# Generated by Django 3.2.8 on 2021-10-11 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc_send', '0003_auto_20211011_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc_request',
            name='file',
            field=models.ImageField(upload_to=''),
        ),
    ]
