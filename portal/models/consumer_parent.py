from auditlog.registry import auditlog
from crum import get_current_user
from django.db import models

from portal.models import TrackedModel


class ConsumerParent(TrackedModel):
    name = models.TextField()

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]


auditlog.register(ConsumerParent)
