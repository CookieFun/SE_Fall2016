from __future__ import unicode_literals

from django.db import models


class UploadFile(models.Model):
    upload_file = models.FileField(upload_to='upload_file/%Y/%m/%d')
