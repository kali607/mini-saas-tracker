from django.db import models
from django.contrib.auth import get_user_model  # ✅ correct import

class Issue(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    severity = models.CharField(
        max_length=10,
        choices=[
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High')
        ]
    )
    created_by = models.ForeignKey(  # ✅ FIXED: no quotes!
        get_user_model(),
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
