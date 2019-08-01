from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
import random
import os

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
    return "clubs/{new_filename}/{final_filename}".format(
                new_filename=new_filename, final_filename=final_filename)


class Club(models.Model):
    LALIGA = 'LG'
    BARCLAYS = 'BL'
    BUNDESLIGA = 'BG'
    SERIA = 'SR'
    BPL = 'BP'
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    manager = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE
    )
    points = models.PositiveIntegerField(default=0)
    ligue_choice = ((LALIGA, 'Laliga'),
                    (BARCLAYS, 'Barclays'),
                    (BUNDESLIGA,'Bundesliga'),
                    (SERIA, 'Seria'),
                    (BPL, 'Bpl',))
    ligue = models.CharField(max_length=2,
            choices=ligue_choice,
            default = LALIGA)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('club_detail', args=[str(self.id)])
