from django.shortcuts import render
from rest_framework import generics, serializers
from request.serializers import RequestSerializer
from request.models import Request
# Create your views here.

class RequestPost(generics.ListCreateAPIView):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()

    def get_queryset(self):
        return super().get_queryset()

    def perform_create(self, serializer):
        print(serializer.data)
        return super().perform_create(serializer)