#! /usr/bin/env python3.9
# -*- coding: utf8 -*-

from rest_framework import serializers
from .models import UploadFileModel, PulseRecognitionModel
from django.utils.translation import gettext_lazy as _


class UploadFileSerializer(serializers.ModelSerializer):
    filename = serializers.CharField(label=_('文件名'), read_only=True, source='file.name')

    class Meta:
        model = UploadFileModel
        fields = '__all__'


class PulseRecognitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PulseRecognitionModel
        fields = '__all__'
