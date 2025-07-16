from django.db import models

class DailyStat(models.Model):
    date = models.DateField()
    status = models.CharField(max_length=20)
    count = models.PositiveIntegerField()

    class Meta:
        unique_together = ("date", "status")