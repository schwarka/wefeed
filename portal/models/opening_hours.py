from auditlog.registry import auditlog
from django.db import models

WEEKDAYS = [
    (1, ("Monday")),
    (2, ("Tuesday")),
    (3, ("Wednesday")),
    (4, ("Thursday")),
    (5, ("Friday")),
    (6, ("Saturday")),
    (7, ("Sunday")),
]


class OpeningHours(models.Model):
    weekday = models.IntegerField(choices=WEEKDAYS)
    from_hour = models.TimeField()
    to_hour = models.TimeField()

    class Meta:
        ordering = ("weekday", "from_hour")
        unique_together = ("weekday", "from_hour", "to_hour")
        verbose_name_plural = "Opening Hours"

    def __str__(self):
        return u"%s: %s - %s" % (
            self.get_weekday_display(),
            self.from_hour,
            self.to_hour,
        )


auditlog.register(OpeningHours)
