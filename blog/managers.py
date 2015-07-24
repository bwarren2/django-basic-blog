from django.db import models
from django.db.models import Q

PUBLIC = 0
LOGIN = 1
PRIVATE = 2


class PublicManager(models.Manager):

    def get_queryset(self):
        return super(PublicManager, self).get_queryset().filter(
            Q(publicity=0)  # Bad hardcoding, but circumvents circular import
        )


class LoginManager(models.Manager):

    def get_queryset(self):
        return super(LoginManager, self).get_queryset().filter(
            Q(publicity=PUBLIC) | Q(publicity=LOGIN)
        )


class PrivateManager(models.Manager):

    def get_queryset(self):
        return super(PrivateManager, self).get_queryset().filter(
            Q(publicity=PUBLIC) | Q(publicity=LOGIN) | Q(publicity=PRIVATE)
        )
