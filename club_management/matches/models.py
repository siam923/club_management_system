from django.db import models
from clubs.models import Club
from django.db.models.signals import post_save
from django.urls import reverse

class Match(models.Model):
    team_1 = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='team_1')
    team_2 = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='team_2')
    score_1 = models.PositiveIntegerField(default=0)
    score_2 = models.PositiveIntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} VS {}'.format(self.team_1, self.team_2)

    def update_points(self):
        if self.score_1 > self.score_2:
            self.team_1.points += 3
            self.team_1.save()
        elif self.score_2 > self.score_1:
            self.team_2.points += 3
            self.team_2.save()
        else:
            self.team_1.points += 1
            self.team_2.points += 1
            self.team_1.save()
            self.team_2.save()

    def get_absolute_url(self):
        return reverse('match_list')


# order create hoar por.. sender match, instance-> order_object jeta create holo
def post_save_points(sender, instance, created, *args, **kwargs):
    if created:
        instance.update_points()

post_save.connect(post_save_points, sender=Match)
