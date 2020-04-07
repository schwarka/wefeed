from auditlog.registry import auditlog
from django.db import models
from django_fsm import FSMField
from django_fsm import transition

from portal.models import TrackedModel


class Order(TrackedModel):
    deliver_on = models.DateTimeField("Delivery Date and Time")
    num_prepacked_meals = models.IntegerField()

    consumer = models.ForeignKey("Consumer", on_delete=models.CASCADE)
    provider = models.ForeignKey(
        "Provider", on_delete=models.CASCADE, blank=True, null=True
    )
    volunteer = models.ForeignKey(
        "Volunteer", on_delete=models.CASCADE, blank=True, null=True
    )

    need_delivery = models.BooleanField()

    status = FSMField(default="waiting_for_review")

    @property
    def order_total(self):
        if self.provider:
            sub_total = self.num_prepacked_meals * self.provider.pre_packaged_meal_price
            if self.need_delivery:
                sub_total += self.provider.delivery_price
            return sub_total

    def __str__(self):
        return f"{self.deliver_on} {self.consumer}"

    class Meta:
        ordering = ["-deliver_on", "id"]

    @transition(
        field=status,
        source="waiting_for_review",
        target="approved",
        custom=dict(button_name="Approve"),
    )
    def approve(self):
        """
        This function may contain side-effects,
        like updating caches, notifying users, etc.
        The return value will be discarded.
        """

    @transition(
        field=status,
        source="waiting_for_review",
        target="denied",
        custom=dict(button_name="Deny"),
    )
    def deny(self):
        """
        This function may contain side-effects,
        like updating caches, notifying users, etc.
        The return value will be discarded.
        """

    @transition(
        field=status,
        source="waiting_for_review",
        target="need_correction",
        custom=dict(button_name="Needs Correction"),
    )
    def need_correction(self):
        """
        This function may contain side-effects,
        like updating caches, notifying users, etc.
        The return value will be discarded.
        """

    @transition(
        field=status,
        source="need_correction",
        target="waiting_for_review",
        custom=dict(button_name="Corrected"),
    )
    def corrected(self):
        """
        This function may contain side-effects,
        like updating caches, notifying users, etc.
        The return value will be discarded.
        """

    @transition(
        field=status,
        source="approved",
        target="matched",
        custom=dict(button_name="Match Success"),
    )
    def match(self):
        """
        This function may contain side-effects,
        like updating caches, notifying users, etc.
        The return value will be discarded.
        """

    @transition(
        field=status,
        source="matched",
        target="delivered",
        custom=dict(button_name="Verified Delivered"),
    )
    def deliver(self):
        """
        This function may contain side-effects,
        like updating caches, notifying users, etc.
        The return value will be discarded.
        """

    @transition(
        field=status,
        source="delivered",
        target="paid",
        custom=dict(button_name="Mark Paid"),
    )
    def paid(self):
        """
        This function may contain side-effects,
        like updating caches, notifying users, etc.
        The return value will be discarded.
        """


auditlog.register(Order)
