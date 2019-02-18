from django.db import models

# Create your models here.

class EmailContact(models.Model):
    from_email = models.EmailField()
    subject = models.CharField(max_length=100)
    content = models.TextField()
