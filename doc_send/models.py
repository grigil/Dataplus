from django.db import models
from django.utils import timezone
import uuid


class doc_request(models.Model):
    CHOICES = (
        ('Получение выписки из адресного реестра', 'Получение выписки из адресного реестра'),
        ('Внесение изменений в адресный реестр', 'Внесение изменений в адресный реестр'),
        ('Удаление адреса из адресного реестра', 'Удаление адреса из адресного реестра'),
        ('Получение выписки из архива', 'Получение выписки из архива'),
    )
    user = models.CharField(max_length=200)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200, choices=CHOICES)
    text = models.TextField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=200)
    result = models.CharField(max_length=200)
    file = models.ImageField(upload_to="media", blank=True)

    def __str__(self):
        return self.id


class registred_docs(models.Model):
    CHOICES = (
        ('Получение выписки из адресного реестра', 'Получение выписки из адресного реестра'),
        ('Внесение изменений в адресный реестр', 'Внесение изменений в адресный реестр'),
        ('Удаление адреса из адресного реестра', 'Удаление адреса из адресного реестра'),
        ('Получение выписки из архива', 'Получение выписки из архива'),
    )
    user = models.CharField(max_length=200)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=200, choices=CHOICES)
    text = models.TextField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=200)
    result = models.CharField(max_length=200)
    file = models.ImageField(upload_to="media", blank=True)

    def __str__(self):
        return self.id
