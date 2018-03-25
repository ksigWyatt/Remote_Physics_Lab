from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class CurrentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    value = serializers.IntegerField()
    created = serializers.DateField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Current` instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Current` instance, given the validated data.
        """
        instance.value = validated_data.get('value', instance.values)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance