import random
import os
from django.db import models
#from django.db.models.signals import pre_save, post_save
#from club_management.utils import unique_slug_generator
from django.urls import reverse
from clubs.models import Club
from django.db.models import Q

def get_filename_ext(filepath):
    """
    returns name and extension of a file e.g .png
    """
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1, 383232)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(
                        new_filename=new_filename, ext=ext)
    return "players/{new_filename}/{final_filename}".format(
                new_filename=new_filename, final_filename=final_filename)

class PlayerQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

    def search(self, query):
        lookups = (Q(name__icontains=query))
        return self.filter(lookups).distinct()


class PlayerManager(models.Manager):
    def get_queryset(self):
        return PlayerQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self):
        return self.get_queryset().featured()

    def search(self, query):
        lookups = Q(name__icontains=query)
        return self.get_queryset().search(query)


class Player(models.Model):
    name = models.CharField(max_length=120)
    goals = models.PositiveIntegerField(null=True, blank=True)
    assists = models.PositiveIntegerField(null=True, blank=True)
    clean_sheets = models.PositiveIntegerField(null=True, blank=True)
    height = models.DecimalField(decimal_places=2, max_digits=8, default=0.0)
    #slug = models.SlugField(blank=True, unique=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=True)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    club = models.ForeignKey(
        Club,
        on_delete=models.CASCADE,
    )

    objects = PlayerManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('player_detail', args=[str(self.id)])
