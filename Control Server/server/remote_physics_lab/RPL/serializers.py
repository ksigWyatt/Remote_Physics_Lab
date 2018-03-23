from rest_framework import serializers

from RPL.models import Rpl


class RplSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Rpl
        fields = ('url', 'id', 'created', 'name', 'user')
        extra_kwargs = {
            'url': {
                'view_name': 'Rpl:rpl-detail',
            }
        }