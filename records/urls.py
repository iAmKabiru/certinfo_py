from django.urls import path
from records.views import CertificateList


urlpatterns = [
    path('certificates', CertificateList.as_view(), name='certificates')
]