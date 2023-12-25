#! /usr/bin/env python3.9
# -*- coding: utf8 -*-
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'upload', views.UploadFileViewSet)
router.register(r'result', views.PulseRecognitionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]