from rest_framework import serializers
import re
from .models import ModelManagement

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
        # Check if model with this name already exists (but exclude current instance for updates)
        existing_query = ModelManagement.objects.filter(model_name=value)
        if self.instance:
            existing_query = existing_query.exclude(model_id=self.instance.model_id)
        
        if existing_query.exists():
            raise serializers.ValidationError("A model with this name already exists.")
        
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        
        if len(value) > 255:
            raise serializers.ValidationError("Name cannot exceed 255 characters.")
        
        # Allow alphanumeric characters, underscores, hyphens, and spaces
        # This is more flexible than the original isalnum() check
        if not re.match(r'^[a-zA-Z0-9_\-\s]+$', value):
            raise serializers.ValidationError("Name can only contain letters, numbers, underscores, hyphens, and spaces.")
        
        return value