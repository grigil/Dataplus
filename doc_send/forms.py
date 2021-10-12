from django.forms import ModelForm
from doc_send.models import *
from django.forms import CharField, ModelForm, HiddenInput
from django.utils.translation import gettext_lazy as _

class doc_request_form(ModelForm):
    class Meta:
        model = doc_request
        fields = ['name', 'file']
        labels = {
                    'name': _('Название услуги'),
                    'file': _('Выберете файл'),
                }

class registred_docs_form(ModelForm):
    hidden_id = CharField(widget=HiddenInput(), required=False)
    class Meta:
        model = registred_docs
        fields = ['text', 'status', 'result']
        labels = {
                    'text': _('Текст документа'),
                    'status': _('Статус заявления'),
                    'result': _('Результат заявления')
                }

