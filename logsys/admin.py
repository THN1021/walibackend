from django.contrib import admin
from .models import LogOrderProtocolStatus, LogOrderStatus, ApiLog

# Register your models here.

admin.site.register([LogOrderProtocolStatus, LogOrderStatus, ApiLog])
