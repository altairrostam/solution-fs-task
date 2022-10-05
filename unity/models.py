from django.db import models
from django.contrib import admin
import uuid
from .utils import FieldNameSubscribedStatus
from django.utils.translation import gettext_lazy as _

class Email(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    emailId = models.EmailField(_('email address'), unique=True)
    status = models.IntegerField(
            choices=FieldNameSubscribedStatus.choices,
            default=FieldNameSubscribedStatus.SUBSCRIBED)
    timestamp= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.emailId

class EmailAdmin(admin.ModelAdmin):
    readonly_fields = ('id','timestamp',)
