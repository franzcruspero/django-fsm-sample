from datetime import datetime

from django.db import models

from django_fsm import FSMField, transition, RETURN_VALUE
from django_fsm_log.decorators import fsm_log_by, fsm_log_description


class BlogPost(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    state = FSMField(default="new", protected=True)

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def can_publish(self):
        if datetime.now().hour > 17:
            return False
        return True

    def can_destroy(self):
        if not self.title:
            return False
        return True

    @fsm_log_by
    @fsm_log_description
    @transition(
        field=state,
        source=["new", "for_moderators"],
        target="published",
        conditions=[can_publish],
        on_error="failed",
    )
    def publish(self):
        """
        This function may contain side-effects,
        like updating caches, notifying users, etc.
        The return value will be discarded.
        """
        pass

    @fsm_log_by
    @fsm_log_description
    @transition(
        field=state,
        source="*",
        target="destroyed",
        conditions=[can_destroy],
        on_error="failed",
    )
    def destroy(self):
        """
        Side effects galore
        """
        pass

    @transition(
        field=state,
        source="new",
        target=RETURN_VALUE("for_moderators", "pending"),
        on_error="failed",
    )
    def pending(self, is_moderator: bool = False):
        return "for_moderators" if is_moderator else "pending"
