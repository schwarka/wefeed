from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from portal.models import Neighborhood


class NeighborhoodResource(resources.ModelResource):
    class Meta:
        model = Neighborhood
        exclude = (
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
        )


class NeighborhoodAdmin(ImportExportModelAdmin):
    resource_class = NeighborhoodResource
    search_fields = [
        "name",
    ]
    readonly_fields = (
        "created_at",
        "created_by",
        "updated_at",
        "updated_by",
    )


admin.site.register(Neighborhood, NeighborhoodAdmin)
