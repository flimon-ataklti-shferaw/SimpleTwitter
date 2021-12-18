from django.urls import reverse_lazy

from rest_framework import serializers

from accounts.models import User


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
        return reverse_lazy("profiles:detail", kwargs={"email": obj.email })
