from django.db import models
from django.contrib.auth.models import User

class Result(models.Model):
    accessionNumber = models.CharField(max_length=10, null=False)
    sopInstanceUid = models.CharField(max_length=60 ,null=False)
    prediction = models.BooleanField(null=False)
    probability = models.DecimalField(null=False,max_digits=3,decimal_places=3)
    modelVersion = models.CharField(max_length=10,null=False)
