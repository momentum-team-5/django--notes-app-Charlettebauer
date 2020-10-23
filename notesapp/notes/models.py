from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta

class Comment(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    poem = models.ForeignKey('Note', on_delete=models.CASCADE)

class Note(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def niceCreated(self):
        nice_created = self.created_at - timedelta(hours=4)
        return nice_created.strftime("Created on %A at %I:%M %p")

    def niceUpdated(self):
        nice_updated = self.updated_at - timedelta(hours=4)
        return nice_updated.strftime("Last updated on %A at %I:%M %p")

    @property
    def comments(self):
        return Comment.objects.filter(note=self)

        

    def __str__(self):
        return f"{self.title}"