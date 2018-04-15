from tastypie.resources import ModelResource
from RPL.models import Rpl, Users
from tastypie.authorization import Authorization

class RplResource(ModelResource):
    class Meta:
        queryset = Rpl.objects.all()
        resource_name = 'variables'
        authorization = Authorization()
        fields = ['values', 'variables']

class UsersResource(ModelResource):
    class Meta:
        queryset = Users.objects.all()
        resource_name = 'queue'
        authorization = Authorization()
        fields = ['ip', 'place']