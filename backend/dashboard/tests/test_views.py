from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from issues.models import Issue
from datetime import date, timedelta

class SeverityChartTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="pass")
        self.client.login(username="test", password="pass")
        Issue.objects.create(title="Issue 1", severity="high", user=self.user)
        Issue.objects.create(title="Issue 2", severity="low", user=self.user)

    def test_chart_data(self):
        response = self.client.get("/api/dashboard/severity-chart/")
        self.assertEqual(response.status_code, 200)
        self.assertTrue("severity" in response.json()[0])
