from rest_framework import serializers
from .models import Cookie_stand


class Cookie_standSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cookie_stand
        fields = "__all__"
