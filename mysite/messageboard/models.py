from __future__ import unicode_literals
from django.db import models

# Create your models here.
class MsgPost(models.Model):
	content = models.TextField()
	datetime = models.DateTimeField(auto_now_add=True)
	index = models.IntegerField(default=0)
	class Meta:
		ordering = ['-datetime']
	
