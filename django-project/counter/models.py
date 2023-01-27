from django.db import models
from django.urls import reverse

class BaseTimestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CountProcess(BaseTimestamp):
    max_count = models.IntegerField()
    current_count = models.IntegerField(default=0)

    def is_complete(self):
        return self.current_count == self.max_count
    
    def __str__(self):
        return f"Count Process #{self.id}"

    def get_absolute_url(self):
        return reverse("counter:counter-log", args=[self.id])