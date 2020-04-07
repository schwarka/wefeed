from django.contrib import admin
from fsm_admin.mixins import FSMTransitionMixin
from import_export import fields
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ManyToManyWidget

from portal.models import Neighborhood
from portal.models import Provider


class ProviderResource(resources.ModelResource):
    neighborhood = fields.Field(
        column_name="neighborhood",
        attribute="neighborhood",
        widget=ManyToManyWidget(Neighborhood, field="id", separator="|"),
    )

    class Meta:
        model = Provider
        exclude = (
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
        )


class ProviderAdmin(FSMTransitionMixin, ImportExportModelAdmin):
    resource_class = ProviderResource
    search_fields = [
        "name",
    ]
    fsm_field = [
        "status",
    ]
    readonly_fields = (
        "created_at",
        "created_by",
        "updated_at",
        "updated_by",
        "status",
    )
    list_filter = [
        "status",
    ]
    list_display = ["name", "address_line_one", "zip", "status"]


admin.site.register(Provider, ProviderAdmin)
