from rest_framework import serializers
from .models import Package, PrerequisitesType, Record, Prerequisites, UserProfile

class PrerequisitesTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrerequisitesType
        fields = ['id', 'description']

class PackageSerializer(serializers.ModelSerializer):
    prerequisites_types = PrerequisitesTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Package
        fields = ['id', 'name', 'prerequisites_types']

class PrerequisitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prerequisites
        fields = ['type', 'note']

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class RecordCreateSerializer(serializers.ModelSerializer):
    prerequisites = PrerequisitesSerializer(many=True, source='record_prerequisites')

    class Meta:
        model = Record
        fields = ['patient', 'supporter', 'package', 'prerequisites']

    def create(self, validated_data):
        prerequisites_data = validated_data.pop('record_prerequisites')
        record = Record.objects.create(**validated_data)

        for prerequisite_data in prerequisites_data:
            Prerequisites.objects.create(record=record, **prerequisite_data)

        return record

    def validate(self, attrs):
        package = attrs['package']
        prerequisites = attrs['record_prerequisites']

        # Get the prerequisite types associated with the package
        package_prerequisite_types = package.prerequisitestype_set.all()

        # Get the prerequisite type IDs
        package_prerequisite_type_ids = set(package_prerequisite_types.values_list('id', flat=True))

        # Get the prerequisite type IDs from the request
        request_prerequisite_type_ids = set(prerequisite['type'].id for prerequisite in prerequisites)

        # Check if all prerequisite type IDs from the package are present in the request
        missing_prerequisite_type_ids = package_prerequisite_type_ids - request_prerequisite_type_ids
        if missing_prerequisite_type_ids:
            raise serializers.ValidationError("All prerequisites for the package must be provided.")

        return attrs
