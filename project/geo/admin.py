from django.contrib import admin
from django.contrib.gis.db import models

from .models import Provider, ServiceArea

admin.site.register(Provider)
admin.site.register(ServiceArea)
