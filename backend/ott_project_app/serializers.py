from rest_framework import serializers
from .models import ott_project_app

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'content',
        )
        model = ott_project_app