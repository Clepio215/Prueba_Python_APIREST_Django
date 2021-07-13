from django.db import models
from django.db.models.base import Model


# Create your models here.

class course(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

class tophistorias(models.Model):
    itemid = models.JSONField()
    created_at = models.TextField()
    


    
def __str__(self):
    return str(self.itemid)
    
