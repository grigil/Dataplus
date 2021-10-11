# Generated by Django 3.2.8 on 2021-10-11 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc_send', '0004_alter_doc_request_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc_request',
            name='user',
            field=models.CharField(default='Null', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doc_request',
            name='file',
            field=models.ImageField(blank=True, upload_to='media'),
        ),
    ]
