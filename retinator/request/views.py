import PIL.Image
from pydicom import dcmread
from rest_framework import generics, status
from rest_framework.response import Response
from request.models import Request
from request.serializers import RequestSerializer

import os
import cv2
import matplotlib
matplotlib.use('agg')
import request.preprocess as pre
# Create your views here.

class RequestPost(generics.ListCreateAPIView):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()

    def get_queryset(self):
        return super().get_queryset()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)

        if serializer.is_valid():
            #self.process_request(serializer.data)
            self.process_image(serializer.data)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        return super().perform_create(serializer)

    def process_request(self, data):
        for dicomHeader in data:
            dicom = self.get_dicom(dicomHeader['dicomPath'])
            image = self.get_image_from_dicom(dicomHeader['dicomPath'])
            #validacion desarrollarlo 
            #result = self.pre_process_dicom(image, dicomHeader['dicomPath'])
            #procesamiento
        pass

    def process_image(self, data):
        for dicomHeader in data:
            #dicom = self.get_dicom(dicomHeader['dicomPath'])
            image = self.get_image(dicomHeader['dicomPath'])
            #validacion desarrollarlo 
            result = self.pre_process_dicom(image, dicomHeader['dicomPath'])
            #procesamiento
        pass

    def get_dicom(self, path):
        dicom = dcmread(path)
        print(dicom)
        return dicom

    def readimage(self, path):
        with open(path, "rb") as f:
            return bytearray(f.read())

    def get_image_from_dicom(self, dicom):
        image = self.get_PIL_image(dicom)
        return image

    def get_image(self, image_path):
        image = cv2.imread(os.path.abspath(image_path), -1)
        return image


    def pre_process_dicom(self, image, image_path, save_path="/tmp"):
        diameter=299 
        success = 0
        try:
            # Load the image and clone it for output.
            #image = cv2.imread(os.path.abspath(image_path), -1)

            processed = pre._resize_and_center_fundus(image, diameter=diameter)

            if processed is None:
                print("Could not preprocess {}...".format(image_path))
            else:
                # Get the save path for the processed image.
                image_filename = pre._get_filename(image_path)
                image_jpeg_filename = "{0}.jpg".format(os.path.splitext(
                                        os.path.basename(image_filename))[0])
                output_path = os.path.join(save_path, image_jpeg_filename)

                # Save the image.
                cv2.imwrite(output_path, processed,
                            [int(cv2.IMWRITE_JPEG_QUALITY), 100])

                success += 1
        except AttributeError as e:
            print(e)
            print("Could not preprocess {}...".format(image_path))

        return success
        
        
        
    def get_PIL_image(self, dicom):
        if ('WindowWidth' not in dicom) or ('WindowCenter' not in dicom):
            bits = dicom.BitsAllocated
            samples = dicom.SamplesPerPixel
            if bits == 8 and samples == 1:
                mode = "L"
            elif bits == 8 and samples == 3:
                mode = "RGB"
            elif bits == 16:
                mode = "I;16"
            else:
                raise TypeError("Don't know PIL mode for %d BitsAllocated "
                                "and %d SamplesPerPixel" % (bits, samples))

            size = (dicom.Columns, dicom.Rows)
            im = PIL.Image.frombuffer(mode, size, dicom.PixelData, "raw", mode, 0, 1)
            return im



   