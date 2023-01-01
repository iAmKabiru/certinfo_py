from rest_framework import serializers
from records.models import Certificate


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = (
            'id',
            'certificate_id', 
            'full_name',
            'address',
            'dob',
            'type',
            'issued_on',
            'expired_on',
            'created',
            'updated'
        )