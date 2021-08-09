import PIL.Image
from pydicom import dcmread
from rest_framework import generics, status
from rest_framework.response import Response
from request.models import Request
from request.serializers import RequestSerializer

# Create your views here.

class RequestPost(generics.ListCreateAPIView):
    serializer_class = RequestSerializer
    queryset = Request.objects.all()

    def get_queryset(self):
        return super().get_queryset()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)

        if serializer.is_valid():
            self.process_request(serializer.data)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
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
        print(dicom)
        return dicom

    def readimage(self, path):
        with open(path, "rb") as f:
            return bytearray(f.read())

    def process_dicom(self, dicom):
        image = self.get_PIL_image(dicom)
        image.save("C:/Users/nicop/Downloads/dicom_image.jpg")
        pass

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