from rest_framework import serializers
from .models import Content, UserRating


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = "__all__"


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRating
        fields = ("user", "content", "rating")
