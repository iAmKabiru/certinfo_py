from rest_framework.generics import ListAPIView
from rest_framework import filters
from records.models import Certificate
from records.serializers import CertificateSerializer
from django_filters.rest_framework import DjangoFilterBackend


class CertificateList(ListAPIView):
    model = Certificate
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields =  ['id', 'certificate_id', 'full_name', 'address', 'type']
    search_fields =  ['id', 'certificate_id', 'full_name', 'address', 'type']
    ordering_fields =  ['id', 'issued_on']