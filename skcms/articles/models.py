#-*- coding: utf-8 -*-
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Tytul")
    content = models.TextField(verbose_name="Zawartosc")
    published = models.DateTimeField(verbose_name="Data publikacji")
    image = models.FileField(upload_to="images/", verbose_name="Obrazek")

    def __unicode__(self):
        return self.title