from django.contrib import admin
from django.urls import path
from request.views import RequestPost

urlpatterns = [
    path('create/', RequestPost.as_view(), name='create_request'),
]
