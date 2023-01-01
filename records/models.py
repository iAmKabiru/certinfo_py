from django.db import models


class Certificate(models.Model):
    certificate_id = models.CharField(max_length=20)
    full_name = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    dob = models.DateField()
    type = models.CharField(max_length=30, choices=(
        ('nin', 'National Identify Document'),
        ('voter', 'Voters Card'),
        ('driver', 'Drivers License')
    ))
    issued_on = models.DateField()
    expired_on = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.certificate_id