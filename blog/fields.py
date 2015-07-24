from django.db.models import DateTimeField
from django.utils import timezone


class AutoDatetimeField(DateTimeField):

    def pre_save(self, model_instance, add):
        return timezone.now()
