from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.utils.translation import gettext_lazy as _

# Create your models here.
class UserCart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=_('user'))
    items = JSONField()