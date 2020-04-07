from tastypie.authentication import ApiKeyAuthentication
from tastypie.authentication import BasicAuthentication
from tastypie.authentication import MultiAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource

from portal.models import Order


class OrderResource(ModelResource):
    class Meta:
        queryset = Order.objects.filter(status="approved")
        resource_name = "order"
        authentication = MultiAuthentication(
            BasicAuthentication(), ApiKeyAuthentication()
        )
        authorization = DjangoAuthorization()
