from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count
from issues.models import Issue

@api_view(['GET'])
def severity_chart(request):
    counts = Issue.objects.values('severity').annotate(count=Count('id'))
    data = {"low": 0, "medium": 0, "high": 0, "critical": 0}
    for item in counts:
        data[item["severity"]] = item["count"]
    return Response(data)
