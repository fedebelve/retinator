from django.db import models

# Create your models here.
class Request(models.Model):
    idPatient = models.PositiveIntegerField(null=False)
    accessionNumber = models.PositiveIntegerField( null=False)
    domain = models.CharField(max_length=3, null=False)
    dicomPath = models.CharField(max_length=70, null=False)
    studyUid = models.CharField(max_length=60, null=False)
    serieUid = models.CharField(max_length=60, null=False)
    sopInstanceUid = models.CharField(max_length=60, null=False)

# class RequestStatus(models.Model):
#     request = models.OneToOneField(Request, on_delete=Mo, null=False)
#     status = models.CharField(max_length=200, null=False)