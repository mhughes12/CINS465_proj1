from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=4, primary_key=True)
    value = models.SmallIntegerField()
    #is_user_value = models.BinaryField(default=False)
