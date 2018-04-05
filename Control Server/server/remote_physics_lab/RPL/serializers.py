from rest_framework import serializers

from RPL.models import Rpl, LANGUAGE_CHOICES, STYLE_CHOICES
from rest_framework import serializers


class RplSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    variables = serializers.CharField(required=False, allow_blank=True, max_length=30)
    style = serializers.IntegerField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Rpl.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.variables = validated_data.get('variables', instance.variables)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance