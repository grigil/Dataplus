from django.db import models
from django.utils import timezone
import uuid

CHOICES = (
    ('Получение выписки из адресного реестра', 'Получение выписки из адресного реестра'),
    ('Внесение изменений в адресный реестр', 'Внесение изменений в адресный реестр'),
    ('Удаление адреса из адресного реестра', 'Удаление адреса из адресного реестра'),
    ('Получение выписки из архива', 'Получение выписки из архива'),
)
CHECKBOX_STATUS = (
    ('Зарегистрировано', 'Зарегистрировано'),
    ('Отклонено', 'Отклонено'),
    ('Отказ', 'Отказ'),
    ('Направлена квитанция на оплату', 'Направлена квитанция на оплату'),
    ('Принято в работу', 'Принято в работу'),
    ('Выполняются работы по заявлению', 'Выполняются работы по заявлению'),
    ('Результаты готовы к выдаче', 'Результаты готовы к выдаче'),
    ('Результаты переданы заявителю', 'Результаты переданы заявителю'),
)
CHECKBOX_RESULT = (
    ('Обработка инфы', 'Обработка инфы'),
    ('Подготовлена справка об отсутствии данных', 'Подготовлена справка об отсутствии данных'),
    ('Сформирована выписка из адресного реестра', 'Сформирована выписка из адресного реестра'),
    ('Внесены изменения в адресный реестр', 'Внесены изменения в адресный реестр'),
    ('Удален адрес из адресного реестра', 'Удален адрес из адресного реестра'),
    ('Сформирована выписка из архива', 'Сформирована выписка из архива'),
)


class doc_request(models.Model):
    user = models.CharField(max_length=200)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200, choices=CHOICES)
    text = models.TextField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=200, choices=CHECKBOX_STATUS)
    result = models.CharField(max_length=200, choices=CHECKBOX_RESULT)
    file = models.ImageField(upload_to="media", blank=True)

    def __str__(self):
        return self.id


class registred_docs(models.Model):
    user = models.CharField(max_length=200)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200, choices=CHOICES)
    text = models.TextField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=200, choices=CHECKBOX_STATUS)
    result = models.CharField(max_length=200, choices=CHECKBOX_RESULT)
    file = models.ImageField(upload_to="media", blank=True)

    def __str__(self):
        return self.id
