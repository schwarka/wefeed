from auditlog.registry import auditlog
from django.db import models

from portal.models import TrackedModel


class ProviderPreference(TrackedModel):
    provider = models.ForeignKey(
        "provider", on_delete=models.CASCADE, related_name="score"
    )
    score = models.DecimalField(max_digits=14, decimal_places=2, default=0.0,)

    def __str__(self):
        return f"{self.name}"


auditlog.register(ProviderPreference)
