from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from portal.models import ProviderParent


class ProviderParentResource(resources.ModelResource):
    class Meta:
        model = ProviderParent
        exclude = (
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
        )


class ProviderParentAdmin(ImportExportModelAdmin):
    resource_class = ProviderParentResource
    search_fields = [
        "name",
    ]
    readonly_fields = (
        "created_at",
        "created_by",
        "updated_at",
        "updated_by",
    )


admin.site.register(ProviderParent, ProviderParentAdmin)
