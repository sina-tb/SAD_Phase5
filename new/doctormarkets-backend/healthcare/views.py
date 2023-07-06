from rest_framework import generics
from .models import Package, Record, PrerequisitesType
from .serializers import PackageSerializer, RecordCreateSerializer, PrerequisitesTypeSerializer

class PackageListView(generics.ListAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class PrerequisitesTypeListView(generics.ListAPIView):
    serializer_class = PrerequisitesTypeSerializer

    def get_queryset(self):
        package_id = self.kwargs['package_id']
        return PrerequisitesType.objects.filter(packages__id=package_id)

class RecordCreateView(generics.CreateAPIView):
    serializer_class = RecordCreateSerializer
