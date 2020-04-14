from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=25, primary_key=True)
    value = models.CharField(max_length=300)
    
