from django.db import models
from django.utils import timezone


# Models based on project but currently simplified

class ProfilePicture(models.Model):
    class ColorChoices(models.TextChoices):
        RED = 'r', '#d4002d'
        GREEN = 'g', '#76b82a'
        TURQUOISE = 't', '#00afcb'
        YELLOW = 'y', '#f7a600'
        ORANGE = 'o', '#ec6608'
        VIOLET = 'v', '#af1280'
        BLUE = 'b', '#005ca9'

    color = models.TextField(choices=ColorChoices.choices)


class Member(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField(null=True)
    level = models.PositiveIntegerField(default=1)
    score = models.PositiveIntegerField(default=0)
    friends = models.ManyToManyField('self', blank=True)

    profile_picture = models.ForeignKey(ProfilePicture, on_delete=models.CASCADE, null=True)


class Type(models.Model):
    is_custom = models.BooleanField(default=False)
    name = models.TextField()
    duration = models.PositiveIntegerField(null=True)


class Habit(models.Model):
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True)
    name = models.TextField()
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    priority = models.PositiveSmallIntegerField(null=True)


class Message(models.Model):
    message = models.TextField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
