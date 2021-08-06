from django.shortcuts import render
from rest_framework import generics, serializers, status
from rest_framework.response import Response
from request.serializers import RequestSerializer
from request.models import Request
from pydicom import dcmread
# Create your views here.

class RequestPost(generics.ListCreateAPIView):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()

    def get_queryset(self):
        return super().get_queryset()


    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data,many=True)

        if serializer.is_valid():

            self.process_request(serializer.data)
            self.perform_create(serializer)
            headers= self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):

        return super().perform_create(serializer)


    def process_request(self, data):

        for dicomHeader in data:            
            dicom = self.get_dicom(dicomHeader['dicomPath'])
            result = self.process_dicom(dicom)
        
        pass

    def get_dicom(self, path):
            dicom = dcmread(path) 
            return dicom

    def process_dicom(self, dicom):
        pass