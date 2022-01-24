from ..models import University, Major
from django.contrib.auth import get_user_model

from rest_framework import serializers
from ..models import Major


class MajorSeializer(serializers.ModelSerializer):
    
    class Meta:
        model = Major
        fields = ('id', 'major_name')