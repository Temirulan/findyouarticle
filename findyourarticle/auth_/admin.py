from .models import MainUser

from django.conf import settings
from django.contrib import admin, messages
from django.contrib.admin.templatetags.admin_urls import add_preserved_filters
from django.contrib.admin.models import LogEntry, DELETION
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import path, reverse
from django.utils import timezone
from django.utils.html import format_html, escape

from io import BytesIO
from itertools import chain


@admin.register(MainUser)
class MainUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name')
    list_filter = ('is_admin', 'is_staff')
    search_fields = ('email', 'full_name')
    ordering = ('-id',)
    fieldsets = (
        (
            'Information',
            {
                'fields': (
                    'full_name','email'
                )
            }
        ),
        ('Permissions', {'fields': ('is_active', 'is_admin', 'is_staff')}),
    )
