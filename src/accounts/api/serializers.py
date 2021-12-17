from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from rest_framework import serializers

User = settings.AUTH_USER_MODEL


class UserDisplaySerializer(serializers.ModelSerializer):
    follower_count = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'email',
            'follower_count',
            'url',
        ]

    def get_follower_count(self, obj):
        return 0

    def get_url(self, obj):
        return reverse_lazy("profiles:detail", kwargs={"email": obj.email})
