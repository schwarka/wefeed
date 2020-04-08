from auditlog.registry import auditlog
from crum import get_current_user
from django.db import models
from django_fsm import FSMField
from django_fsm import transition
from phonenumber_field.modelfields import PhoneNumberField

from portal.models import TrackedModel


class Consumer(TrackedModel):
    parent = models.ForeignKey(
        "ConsumerParent", null=True, blank=True, on_delete=models.SET_NULL
    )
    name = models.TextField()

    first_name = models.TextField()
    last_name = models.TextField()
    phone = models.CharField(max_length=20, null=False, blank=False)
    email = models.TextField()

    address_line_one = models.TextField()
    address_line_two = models.TextField(null=True, blank=True)
    city = models.TextField(default="Columbus")
    state = models.TextField(default="OH")
    zip = models.TextField()

    neighborhood = models.ForeignKey("Neighborhood", on_delete=models.CASCADE)

    status = FSMField(default="waiting_for_review")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]

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
        source=["approved"],
        target="withdrawn",
        custom=dict(button_name="Withdrawal"),
    )
    def withdrawal(self):
        """
        This function may contain side-effects,
        like updating caches, notifying users, etc.
        The return value will be discarded.
        """


auditlog.register(Consumer)
