import datetime

from django.db import models
from embed_video.fields import EmbedVideoField
from django.utils import timezone
from django.db import models


# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class To_learn(models.Model):
	name = models.CharField(max_length=100)
	learned = models.BooleanField(default=False)
	category = models.CharField(max_length=100)
	date_added = models.DateTimeField('trick added', auto_now_add=True, auto_now=False,)
	video = EmbedVideoField(blank=True)
	def __str__(self):
		return self.name