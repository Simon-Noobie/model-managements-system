from django.db import models
from django.contrib.auth.models import User
import json

class ModelManagement(models.Model):
    model_id = models.AutoField(primary_key=True)
    model_name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    feature = models.JSONField(
        blank=True,
        default=list,
        help_text="List of features for the model"
    )
    target = models.JSONField(
        blank=True,
        default=list,
        help_text="List of target variables for the model"
    )
    datatype = models.JSONField(
        blank=True,
        default=list,
        help_text="List of data types for the model features"
    )
    
    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.model_name  # Fixed: was self.name
