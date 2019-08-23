from django.contrib import admin
from .models import *


class ManagementAdmin(admin.ModelAdmin):
    list_display = ['task', 'count', 'started', 'finished', 'state']


admin.site.register(ManagementLog, ManagementAdmin)