from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from ..models import User

admin.site.site_header = mark_safe("<div>Food Delivery Portal</div>")
admin.site.site_title = "Make that food - Get that food"
admin.site.index_title = "Fulfillment"

from .consumer import ConsumerAdmin
from .consumer_parent import ConsumerParentAdmin
from .neighborhood import NeighborhoodAdmin
from .opening_hours import OpeningHoursAdmin
from .order import OrderAdmin
from .provider import ProviderAdmin
from .provider_parent import ProviderParentAdmin
from .volunteer import VolunteerAdmin
from .provider_preference import ProviderPreferenceAdmin

admin.site.register(User, UserAdmin)
