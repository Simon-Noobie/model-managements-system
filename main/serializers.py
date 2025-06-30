from rest_framework import serializers

from .models import ModelManagement  # Replace with your actual model(s)

class ModelManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelManagement
        fields = ['model_id', 'model_name', 'created_at', 'feature', 'target', 'datatype']
        read_only_fields = ['created_at']  

    def validate_feature(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Feature must be a list.")
        return value
    
    def validate_target(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Target must be a list.")
        return value
    
    def validate_datatype(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Datatype must be a list.")
        return value

    def validate_model_name(self, value):
        if ModelManagement.objects.filter(model_name=value).exists():
            raise serializers.ValidationError("A model with this name already exists.")
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        if len(value) > 255:
            raise serializers.ValidationError("Name cannot exceed 255 characters.")
        if not value.isalnum():
            raise serializers.ValidationError("Name must be alphanumeric.")
        return value