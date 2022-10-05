from django.utils.translation import gettext_lazy as _
from django.db import models

class FieldNameSubscribedStatus(models.IntegerChoices):
    UNSUBSCRIBED = 0,_('Unsubscribed')
    SUBSCRIBED =1,_('Subscribed')