from django.db import models

# Create your models here.
class Team(models.Model):
    client = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    proposal_text = models.TextField(blank=True)
