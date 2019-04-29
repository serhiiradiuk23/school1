from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=250)
	datetime = models.DateTimeField()
	content = models.TextField(max_length=100000)

	def _unicode_(self):
		return self.title

	def get_absolute_url(self):
		return "/blog/%i" % self.id
