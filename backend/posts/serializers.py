from rest_framework import serializers
from .models import View


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )
        model = View