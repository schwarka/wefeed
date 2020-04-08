from auditlog.registry import auditlog
from django.db import models
from django_fsm import FSMField
from django_fsm import transition
from phonenumber_field.modelfields import PhoneNumberField

from portal.models import TrackedModel


class Provider(TrackedModel):
    parent = models.ForeignKey(
        "ProviderParent", null=True, blank=True, on_delete=models.SET_NULL
    )
    name = models.TextField("Your Restaurant Name")
    description = models.TextField(
        "Please provide a name for your meal and a list of main ingredients"
    )

    first_name = models.TextField(null=True, blank=True)
    last_name = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=20, null=False, blank=False)

    operations_name = models.TextField(
        "Operations point person name", blank=True, null=True
    )
    operations_email = models.TextField(
        "Operations point person email", blank=True, null=True
    )

    marketing_name = models.TextField(
        "Marketing point person name", blank=True, null=True
    )
    marketing_email = models.TextField(
        "Marketing point person email", blank=True, null=True
    )

    address_line_one = models.TextField()
    address_line_two = models.TextField(null=True, blank=True)
    zip = models.TextField()

    pre_packaged_meal_price = models.DecimalField(
        max_digits=14, decimal_places=2, default=6.0
    )
    delivery_price = models.DecimalField(max_digits=14, decimal_places=2, default=0.0)

    pickup = models.NullBooleanField()
    delivery = models.NullBooleanField()

    able_to_prepare_prepacked_meals = models.NullBooleanField(
        "Are you able to prepare individually packaged meals?"
    )
    servings_per_shift = models.IntegerField(
        "How many servings you can prepare on one shift if packaged in bulk?",
        blank=True,
        null=True,
    )

    capacity_to_package_bulk = models.NullBooleanField(
        "Do you have the capacity to package food in bulk?"
    )
    safely_operate_kitchen = models.NullBooleanField(
        "Will you be able to safely operate your kitchen?"
    )

    neighborhood = models.ManyToManyField("Neighborhood")

    website = models.URLField(null=True, blank=True)

    opening_hours = models.ManyToManyField(
        "OpeningHours",
        verbose_name="List all available days of the week and times you could prepare and provide meals",
        blank=True,
    )

    status = FSMField(default="waiting_for_review")

    def __str__(self):
        return f"{self.name} ({self.pre_packaged_meal_price})"

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


auditlog.register(Provider)
