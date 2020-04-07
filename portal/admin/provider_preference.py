from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from portal.models import ProviderPreference


class ProviderPreferenceResource(resources.ModelResource):
    class Meta:
        model = ProviderPreference
        exclude = (
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
        )


class ProviderPreferenceAdmin(ImportExportModelAdmin):
    resource_class = ProviderPreferenceResource
    search_fields = [
        "name",
    ]
    readonly_fields = (
        "created_at",
        "created_by",
        "updated_at",
        "updated_by",
    )
    list_display = ["provider", "score"]


admin.site.register(ProviderPreference, ProviderPreferenceAdmin)
