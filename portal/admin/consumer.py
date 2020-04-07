from django.contrib import admin
from fsm_admin.mixins import FSMTransitionMixin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from portal.models import Consumer


class ConsumerResource(resources.ModelResource):
    class Meta:
        model = Consumer
        exclude = (
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
        )


class ConsumerAdmin(FSMTransitionMixin, ImportExportModelAdmin):
    resource_class = ConsumerResource
    search_fields = [
        "name",
    ]
    fsm_field = [
        "status",
    ]
    readonly_fields = [
        "created_at",
        "created_by",
        "updated_at",
        "updated_by",
        "status",
    ]
    list_display = ["name", "neighborhood", "address_line_one", "city", "zip", "status"]
    list_filter = [
        "status",
    ]


admin.site.register(Consumer, ConsumerAdmin)
