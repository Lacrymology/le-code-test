from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Stream(models.Model):
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)

    photo = models.ForeignKey('items.PhotoItem', blank=True, null=True)
    tweet = models.ForeignKey('items.TweetItem', blank=True, null=True)

    def clean(self):
        if not (self.photo or self.tweet):
            raise ValidationError("Stream must have either a tweet or a photo")
