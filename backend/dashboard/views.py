from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# any other imports you need...

class SeverityChartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # your logic here
        return Response({"data": []})
