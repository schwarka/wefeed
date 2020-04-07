from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from portal.models import ConsumerParent


class ConsumerParentResource(resources.ModelResource):
    class Meta:
        model = ConsumerParent
        exclude = (
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
        )


class ConsumerParentAdmin(ImportExportModelAdmin):
    resource_class = ConsumerParentResource
    search_fields = [
        "name",
    ]
    readonly_fields = (
        "created_at",
        "created_by",
        "updated_at",
        "updated_by",
    )


admin.site.register(ConsumerParent, ConsumerParentAdmin)
