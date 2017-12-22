import hashlib

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify

from autoslug import AutoSlugField
from django_extensions.db.models import TimeStampedModel

from users.models import OwnerProfile


class SongQuerySet(models.QuerySet):

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.TextField(max_length=100, primary_key=True)
    genre = models.TextField(max_length=100)
    image = models.ImageField(upload_to='group_photos')

    def __str__(self):
        return self.name


def get_slug(instance):
    group = ''
    if instance.group:
        group = instance.group.name
    return slugify('{}-{}'.format(instance.name, group))


class Song(models.Model):
    owner = models.ForeignKey(OwnerProfile)
    group = models.ForeignKey(Group)
    #group = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=5000)
    #objects = SongQuerySet.as_manager()

    def get_absolute_url(self):
        return reverse('songs:detail', kwargs={'pk_or_slug': id})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']

# CREATE TABLE test_songs (id int, song_name VARCHAR(50), group_name VARCHAR(50), song_text VARCHAR(2000),


# class Songs(models.Model):
#     song_name = models.CharField(max_length=50)
#     group_name = models.CharField(max_length=50)
#     song_text = models.CharField(max_length=2000)
#     song_accords = models.CharField(max_length=100)

# CREATE TABLE test_groups (id INT, group_name VARCHAR(50), genre VARCHAR(50), group_members VARCHAR(200),
# image_url VARCHAR(250), description VARCHAR(500));

# class Groups(models.Model):
    #     group_name = models.CharField(max_length=50)
    #     genre = models.CharField(max_length=50)
    #     group_members = models.CharField(max_length=50)
    #     image_url = models.CharField(max_length=50)
    #     description = models.CharField(max_length=500)