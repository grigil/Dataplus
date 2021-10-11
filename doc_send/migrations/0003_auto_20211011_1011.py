# Generated by Django 3.2.8 on 2021-10-11 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc_send', '0002_auto_20211011_0220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc_request',
            name='file',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='doc_request',
            name='name',
            field=models.CharField(choices=[('Получение выписки из адресного реестра', 'Получение выписки из адресного реестра'), ('Внесение изменений в адресный реестр', 'Внесение изменений в адресный реестр'), ('Удаление адреса из адресного реестра', 'Удаление адреса из адресного реестра'), ('Получение выписки из архива', 'Получение выписки из архива')], max_length=200),
        ),
    ]
