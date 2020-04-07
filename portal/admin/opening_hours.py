from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from portal.models import OpeningHours


class OpeningHoursResource(resources.ModelResource):
    class Meta:
        model = OpeningHours
        exclude = (
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
        )


class OpeningHoursAdmin(ImportExportModelAdmin):
    resource_class = OpeningHoursResource
    search_fields = [
        "name",
    ]


admin.site.register(OpeningHours, OpeningHoursAdmin)
