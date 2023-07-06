from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import UserProfile, Package, Record, PrerequisitesType, Prerequisites

class RecordCreateTest(APITestCase):
    def setUp(self):
        self.package = Package.objects.create(name='Test Package')

        # Create prerequisite types and associate them with the package
        self.prerequisite_type1 = PrerequisitesType.objects.create(description='Blood Test')
        self.prerequisite_type2 = PrerequisitesType.objects.create(description='X-ray Image')
        self.prerequisite_type1.packages.add(self.package)
        self.prerequisite_type2.packages.add(self.package)
        self.patient = UserProfile.objects.create(first_name='John', last_name='Doe', type=UserProfile.UserType.PATIENT)
        self.supporter = UserProfile.objects.create(first_name='Alice', last_name='Smith', type=UserProfile.UserType.SUPPORTER)

    def test_create_record_with_prerequisites(self):
        prerequisites = [
            {
                "type": self.prerequisite_type1.id,
                "note": "Blood test sample result"
            },
            {
                "type": self.prerequisite_type2.id,
                "note": "X-ray image report"
            }
        ]
        data = {
            "patient": self.patient.id,
            "supporter": self.supporter.id,
            "package": self.package.id,
            "prerequisites": prerequisites
        }
        url = reverse('record-create')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Record.objects.count(), 1)
        self.assertEqual(Record.objects.first().patient_id, self.patient.id)
        self.assertEqual(Record.objects.first().supporter_id, self.supporter.id)
        self.assertEqual(Record.objects.first().package_id, self.package.id)
        self.assertEqual(Prerequisites.objects.filter(record=Record.objects.first()).count(), len(prerequisites))

    def test_create_record_without_prerequisites(self):
        data = {
            "patient": self.patient.id,
            "supporter": self.supporter.id,
            "package": self.package.id
        }
        url = reverse('record-create')
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Record.objects.count(), 0)
