from django.db import models
from crum import get_current_user
from django.contrib.auth import get_user_model


class TrackedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        get_user_model(),
        blank=True,
        null=True,
        default=None,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_created_by",
    )

    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        get_user_model(),
        blank=True,
        null=True,
        default=None,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_updated_by",
    )

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user
        super(TrackedModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
