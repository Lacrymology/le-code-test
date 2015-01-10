from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class ActiveStreamManager(models.Manager):
    def get_queryset(self):
        return super(ActiveStreamManager, self).get_queryset().filter(
            models.Q(photo__deleted=False) | models.Q(tweet__deleted=False))


class Stream(models.Model):
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)

    photo = models.ForeignKey('items.PhotoItem', blank=True, null=True)
    tweet = models.ForeignKey('items.TweetItem', blank=True, null=True)

    objects = models.Manager()
    active = ActiveStreamManager()

    def clean(self):
        if not (self.photo or self.tweet):
            raise ValidationError("Stream must have either a tweet or a photo")
