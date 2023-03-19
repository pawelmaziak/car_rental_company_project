#-*- coding: utf-8 -8-
from django.db import models

class CustomHtml(models.Model):
	title = models.CharField(max_length=150, verbose_name="Tytuł")
	sourcehtml = models.TextField(verbose_name="Kod HTML")
	image = models.FileField(upload_to="images/", verbose_name="Obrazek")
	def __unicode__(self):
		return self.title
