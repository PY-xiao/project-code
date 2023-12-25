#! /usr/bin/env python3.9
# -*- coding: utf8 -*-
import os

from django.db import models
from utils.audit_model import FullAuditMixin
from django.utils.translation import gettext_lazy as _

from utils.data_cleaners import WaveProgress


class UploadFileModel(FullAuditMixin):
    """
    用户上传文件存储
    """

    class IsPublicChoices(models.IntegerChoices):
        OK = (1, _('公开'))
        No = (0, _('不公开'))

    file = models.FileField(_('上传文件'))
    is_public = models.IntegerField(_('是否公开'), default=IsPublicChoices.OK, choices=IsPublicChoices.choices)

    def save(self, *args, **kwargs):
        adding_flag = self._state.adding
        super(UploadFileModel, self).save(*args, **kwargs)
        if adding_flag:
            file_name = self.file
            os_path = os.getcwd()
            file_path = os_path + f'/media/{file_name}'
            cleaner = WaveProgress()
            cleaner.Progress(file_path)


class PulseRecognitionModel(FullAuditMixin):
    """
    脉象识别
    """

    class ResultsChoices(models.IntegerChoices):
        Yes = (1, _('是脉象数据'))
        No = (0, _('不是脉象数据'))

    file_name = models.CharField(_('文件名'), max_length=255)
    results = models.CharField(_('脉象识别结果'), max_length=255, default=ResultsChoices.No, choices=ResultsChoices.choices)
