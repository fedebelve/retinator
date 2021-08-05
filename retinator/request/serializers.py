from django.db.models import fields
from rest_framework import serializers
from .models import Request

class RequestSerializer(serializers.ModelSerializer):
    #idPatient = serializers.ReadOnlyField()

    class Meta:
        model = Request
        fields = ['idPatient', 'accessionNumber', 'domain', 'dicomPath', 'studyUid', 'serieUid', 'sopInstanceUid']