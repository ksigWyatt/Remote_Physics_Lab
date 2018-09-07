from tastypie.resources import ModelResource
from RPL.models import Rpl, Users
from tastypie.authorization import Authorization

class RplResource(ModelResource):
    class Meta:
        queryset = Rpl.objects.all()
        resource_name = 'variables'
        authorization = Authorization()

class UsersResource(ModelResource):
    class Meta:
        queryset = Users.objects.all()
        resource_name = 'queue'
        authorization = Authorization()