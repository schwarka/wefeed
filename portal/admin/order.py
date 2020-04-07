from admin_comments.admin import CommentInline
from django.contrib import admin
from fsm_admin.mixins import FSMTransitionMixin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from portal.models import Consumer
from portal.models import Order
from portal.models import Provider
from portal.models import Volunteer


class ExpandedCommentInline(CommentInline):
    classes = None


class OrderResource(resources.ModelResource):
    class Meta:
        model = Order
        exclude = (
            "created_at",
            "created_by",
            "updated_at",
            "updated_by",
        )


class OrderAdmin(FSMTransitionMixin, ImportExportModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        if db_field.name == "volunteer":
            kwargs["queryset"] = Volunteer.objects.filter(status="approved")

        if db_field.name == "provider":
            kwargs["queryset"] = Provider.objects.filter(status="approved")

        if db_field.name == "consumer":
            kwargs["queryset"] = Consumer.objects.filter(status="approved")

        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    resource_class = OrderResource
    inlines = [
        ExpandedCommentInline,
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
    list_filter = [
        "status",
    ]
    list_display = [
        "deliver_on",
        "num_prepacked_meals",
        "consumer",
        "provider",
        "volunteer",
        "status",
        "order_total",
    ]

    # def _total(self):
    #     return self.num


admin.site.register(Order, OrderAdmin)
