from django.db import models
from django.contrib.auth.models import User


class ItemAbstract(models.Model):
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __unicode__(self):
        deleted = "[x] " if self.deleted else ""
        return "{deleted}{klass} #{id} ({user})".format(
            deleted=deleted, klass=self.__class__.__name__,
            id=self.id, user=self.user)


class PhotoItem(ItemAbstract):
    image = models.ImageField()

    def url(self):
        return self.image.url


class TweetItem(ItemAbstract):
    text = models.CharField(max_length=150)
