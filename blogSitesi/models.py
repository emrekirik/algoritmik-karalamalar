from django.db import models
from django.utils import timezone


class Gonderi(models.Model):
    baslik = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    tag = models.CharField(max_length=300, blank=True, null=True)

    def yayinla(self):
        self.pub_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.baslik