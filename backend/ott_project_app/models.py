from django.db import models


class ott_project_app(models.model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.title