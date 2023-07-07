from django.db import models
from django.utils.translation import gettext_lazy as _

class UserProfile(models.Model):
    first_name = models.CharField(
        max_length=512,
        blank=False,
        null=False,
    )

    last_name = models.CharField(
        max_length=512,
        blank=False,
        null=False,
    )
    class UserType(models.TextChoices):
        SUPPORTER = '1', _('Supporter')
        PATIENT = '0', _('Patient')

    type = models.CharField(
        max_length=2,
        choices=UserType.choices,
        default=UserType.PATIENT
    )

    class UserStatus(models.TextChoices):
        ACTIVE = 'AC', _('Active')
        INACTIVE = 'IN', _('Inactive')

    status = models.CharField(
        max_length=2,
        choices=UserStatus.choices,
        default=UserStatus.ACTIVE
    )

class PrerequisitesType(models.Model):
    description = models.CharField(max_length=100)
    packages = models.ManyToManyField('Package')

class Prerequisites(models.Model):
    type=models.ForeignKey('PrerequisitesType', on_delete=models.CASCADE)
    record=models.ForeignKey('Record', on_delete=models.CASCADE)
    note=models.CharField(max_length=100)
    
class Package(models.Model):
    name=models.CharField(max_length=20)  
    
class Record(models.Model):
    patient = models.ForeignKey('UserProfile', related_name='record_patient', on_delete=models.CASCADE)
    supporter = models.ForeignKey('UserProfile', related_name='record_supporter', on_delete=models.CASCADE)
    package = models.ForeignKey('Package', on_delete=models.CASCADE)