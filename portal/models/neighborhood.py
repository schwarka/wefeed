from auditlog.registry import auditlog
from crum import get_current_user
from django.db import models

from portal.models import TrackedModel


class Neighborhood(TrackedModel):
    name = models.TextField()
    zip_code = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]


auditlog.register(Neighborhood)
