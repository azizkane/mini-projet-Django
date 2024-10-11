from rest_framework import serializers
from ..models import Dirigeant


class DirigeantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dirigeant
        fields = '__all__'

