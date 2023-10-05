from rest_framework import serializers
from .models import Content, Rating

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ['id', 'title', 'text']