from django.db import models
from django.db.models.fields import CharField


class Language(models.Model):
    name = models.CharField(max_length=50)
    paradigm = CharField(max_length=50)

    def __str__(self):
        return self.name
