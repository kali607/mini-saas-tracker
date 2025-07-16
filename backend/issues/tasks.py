from celery import shared_task
from .models import Issue
from datetime import date
from stats.models import DailyStat

@shared_task
def aggregate_issues():
    today = date.today()
    stats = Issue.objects.values('status').annotate(count=models.Count('id'))
    for stat in stats:
        DailyStat.objects.update_or_create(
            date=today,
            status=stat['status'],
            defaults={'count': stat['count']},
        )