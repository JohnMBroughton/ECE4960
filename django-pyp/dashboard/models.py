# Create your models here.
from django.db import models
#from django.db.models import Model

class RFID(models.Model):
    Lot = models.CharField(max_length=200)
    RFID = models.IntegerField(default=0)
	#
class LotSize(models.Model):
    name = models.CharField(max_length=200)
    num_spaces = models.IntegerField(default=0)
