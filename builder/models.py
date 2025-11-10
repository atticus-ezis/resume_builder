from django.db import models


# Create your models here.
class JobApplication(models.Model):
    company_name = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    cover_letter_content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name
