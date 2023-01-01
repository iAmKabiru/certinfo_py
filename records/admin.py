from django.contrib import admin
from .models import Certificate


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('id', 'certificate_id', 'full_name', 'type')
    list_filter = ('type',)
