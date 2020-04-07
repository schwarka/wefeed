from auditlog.registry import auditlog
from django.db import models
from django_fsm import FSMField
from django_fsm import transition
from phonenumber_field.modelfields import PhoneNumberField

from portal.models import TrackedModel


class Volunteer(TrackedModel):
    first_name = models.TextField()
    last_name = models.TextField()
    phone = PhoneNumberField()
    email = models.TextField()

    address_line_one = models.TextField()
    address_line_two = models.TextField(null=True, blank=True)
    city = models.TextField()
    state = models.TextField()
    zip = models.TextField()

    neighborhood = models.ForeignKey("Neighborhood", on_delete=models.CASCADE)

    status = FSMField(default="waiting_for_review")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.neighborhood}"

    class Meta:
        ordering = ["id"]
        unique_together = ["phone", "email"]

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


auditlog.register(Volunteer)
