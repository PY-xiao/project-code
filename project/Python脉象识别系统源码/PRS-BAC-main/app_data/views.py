#! /usr/bin/env python3.9
# -*- coding: utf8 -*-
import os
import csv
import logging

from django.db.models import Q
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import UploadFileModel, PulseRecognitionModel
from .serializers import UploadFileSerializer, PulseRecognitionSerializer
from utils.get_pred import get_pred

logger = logging.getLogger(__name__)


class UploadFileViewSet(ModelViewSet):
    queryset = UploadFileModel.objects.all()
    serializer_class = UploadFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Determine if the user is admin, if yes return all, not then return rules with status 1
        """
        print(self.request.user)
        if self.request.user.is_staff:
            return UploadFileModel.objects.all()
        id = self.request.user.id
        return UploadFileModel.objects.filter(Q(created_by_id=id) | Q(is_public=1))

    def create(self, request, *args, **kwargs):
        print(f"create data:{request.data}")
        return super(UploadFileViewSet, self).create(request, *args, **kwargs)

    @action(detail=False, methods=['post'])
    def show_data(self, request):
        data = request.data
        file_name = data['file_name']
        file_path = os.getcwd() + f'/media/{file_name}'
        print(f"file_path:{file_path}")
        data_list = []
        with open(file_path, "r", encoding="utf-8") as f:
            data = csv.reader(f)
            for item in data:
                data_list.append(list(item))

        return Response({'data_list': data_list})


class PulseRecognitionViewSet(ModelViewSet):
    queryset = PulseRecognitionModel.objects.all()
    serializer_class = PulseRecognitionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Determine if the user is admin, if yes return all, not then return rules with status 1
        """
        print(self.request.user)
        if self.request.user.is_staff:
            return PulseRecognitionModel.objects.all()
        id = self.request.user.id
        return PulseRecognitionModel.objects.filter(created_by_id=id)

    def create(self, request, *args, **kwargs):
        print(f"old request data:{request.data}")
        data = request.data
        file_name = data['file_name']
        print(f"file_name:{file_name}")
        os_path = os.getcwd()
        file_path = os_path + f'/media/{file_name}'
        results = get_pred(file_path)
        request.data['results'] = results
        print(f"new reqeust data:{request.data}")
        return super(PulseRecognitionViewSet, self).create(request, *args, **kwargs)
