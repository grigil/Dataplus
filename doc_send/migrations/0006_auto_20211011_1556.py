# Generated by Django 3.2.8 on 2021-10-11 12:56

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('doc_send', '0005_auto_20211011_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='registred_docs',
            fields=[
                ('user', models.CharField(max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[('Получение выписки из адресного реестра', 'Получение выписки из адресного реестра'), ('Внесение изменений в адресный реестр', 'Внесение изменений в адресный реестр'), ('Удаление адреса из адресного реестра', 'Удаление адреса из адресного реестра'), ('Получение выписки из архива', 'Получение выписки из архива')], max_length=200)),
                ('text', models.TextField(max_length=200)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('Зарегистрировано', 'Зарегистрировано'), ('Отказ', 'Отказ'), ('Направлена квитанция на оплату', 'Направлена квитанция на оплату'), ('Принято в работу', 'Принято в работу'), ('Выполняются работы по заявлению', 'Выполняются работы по заявлению'), ('Результаты готовы к выдаче', 'Результаты готовы к выдаче'), ('Результаты переданы заявителю', 'Результаты переданы заявителю')], max_length=200)),
                ('result', models.CharField(choices=[('Обработка инфы', 'Обработка инфы'), ('Подготовлена справка об отсутствии данных', 'Подготовлена справка об отсутствии данных'), ('Сформирована выписка из адресного реестра', 'Сформирована выписка из адресного реестра'), ('Внесены изменения в адресный реестр', 'Внесены изменения в адресный реестр'), ('Удален адрес из адресного реестра', 'Удален адрес из адресного реестра'), ('Сформирована выписка из архива', 'Сформирована выписка из архива')], max_length=200)),
                ('file', models.ImageField(blank=True, upload_to='media')),
            ],
        ),
        migrations.AlterField(
            model_name='doc_request',
            name='result',
            field=models.CharField(choices=[('Обработка инфы', 'Обработка инфы'), ('Подготовлена справка об отсутствии данных', 'Подготовлена справка об отсутствии данных'), ('Сформирована выписка из адресного реестра', 'Сформирована выписка из адресного реестра'), ('Внесены изменения в адресный реестр', 'Внесены изменения в адресный реестр'), ('Удален адрес из адресного реестра', 'Удален адрес из адресного реестра'), ('Сформирована выписка из архива', 'Сформирована выписка из архива')], max_length=200),
        ),
        migrations.AlterField(
            model_name='doc_request',
            name='status',
            field=models.CharField(choices=[('Зарегистрировано', 'Зарегистрировано'), ('Отказ', 'Отказ'), ('Направлена квитанция на оплату', 'Направлена квитанция на оплату'), ('Принято в работу', 'Принято в работу'), ('Выполняются работы по заявлению', 'Выполняются работы по заявлению'), ('Результаты готовы к выдаче', 'Результаты готовы к выдаче'), ('Результаты переданы заявителю', 'Результаты переданы заявителю')], max_length=200),
        ),
    ]
